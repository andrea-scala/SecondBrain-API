
from groq import Groq
from core.config import GROQ_API_KEY
from agent.tools import tools, count_documents, search_documents
import json
client = Groq(api_key=GROQ_API_KEY)

# Map function names to implementations
available_functions = {
    "count_documents": count_documents,
    "search_documents": search_documents,
}

def execute_tool_call(tool_call):
    function_name = tool_call.function.name
    function_to_call = available_functions[function_name]
    function_args = json.loads(tool_call.function.arguments) or {}
    result = function_to_call(**function_args)
    return result

def call_with_tools_and_retry(messages, tools, max_retries=3):
    temperature = 1.0
    for attempt in range(max_retries):
        try:
            return client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                tools=tools,
                temperature=temperature,
                tool_choice="auto"
            )
        except Exception as e:
            if hasattr(e, 'status_code') and e.status_code == 400:
                if attempt < max_retries - 1:
                    temperature = max(temperature - 0.2, 0.2)
                    continue
            raise e
    raise Exception("Failed to generate valid tool calls after retries")

def run_agent(prompt: str):
    messages = [
    {
        "role": "system",
        "content": "You are a document assistant. You have access to tools to search and count uploaded documents. Always use the tools to answer questions about documents. Trust the tool results."
    },
    {"role": "user", "content": prompt}
]
    response = call_with_tools_and_retry(messages, tools)
    messages.append(response.choices[0].message)
    # 2. Check for tool calls
    if response.choices[0].message.tool_calls:
        # 3. Execute each tool call (using the helper function from step 2)
        for tool_call in response.choices[0].message.tool_calls:
            function_response = execute_tool_call(tool_call)
            
            # Add tool result to messages
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": tool_call.function.name,
                "content": str(function_response)
            })
        
        # 4. Send results back and get final response
        final = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )
        return final.choices[0].message.content
    return response.choices[0].message.content