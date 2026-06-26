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
                    "query": {
                        "type": "string",
                        "description": "The question of the user"
                    }
                },
                "required": [
                    "query"
                ]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "count_documents",
            "description": "Use this tool when the user wants to know how many documents have been uploaded, not their content.",
            "parameters": {
    "type": "object",
    "properties": {}
}
        },
    }
]

def search_documents(query:str):
    return retrieve(query)

def count_documents():
    return collection.count()