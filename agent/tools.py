from rag.pipeline import retrieve, collection
tools = [
    {
        "type": "function",
        "function": {
            "name": "search_documents",
            "description": "Use this tool when users asks questions about the content of a document",
            "parameters": {
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "The question of the user"
                    }
                },
                "required": [
                    "prompt"
                ]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "count_documents",
            "description": "Use this tool when the user wants to know how many documents have been uploaded, not their content.",
        }
    }
]

def search_documents(prompt:str):
    return retrieve(prompt)

def count_documents():
    return collection.count()