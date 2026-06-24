from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunking(text, cs=500, co=100):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=cs, chunk_overlap=co, add_start_index=True)
    return text_splitter.split_text(text)