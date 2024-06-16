import os
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pdf_combiner import combine_pdfs

def save_vectorstore(chunks):
  vectorstore = Chroma.from_documents(
    documents=chunks, 
    embedding=OllamaEmbeddings(model="nomic-embed-text",show_progress=True),
    collection_name="local-rag",
    persist_directory="chroma_vector_db"
)
  print("\nSaved vectorstore to chroma_vector_db.\n")
  return vectorstore

def get_vectorstore(chunks):
  if os.path.exists("chroma_vector_db"):
    load_vectorstore = Chroma(persist_directory="chroma_vector_db",
                              embedding_function=OllamaEmbeddings(model="nomic-embed-text"),
                              collection_name="local-rag" )
    print("\nFound chroma_vector_db. Loaded vectorstore.\n")
    return load_vectorstore
  else:
    return save_vectorstore(chunks)
  
def get_chunks(local_path):
  if local_path:
    loader = UnstructuredPDFLoader(file_path=local_path)
    data = loader.load()
  else:
    combine_pdfs()

  text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=50)
  chunks = text_splitter.split_documents(data)
  return chunks

def get_retriever(vectorstore, ollama):
    QUERY_PROMPT = PromptTemplate(
      input_variables=["question"],
      template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are an AI specializing in writing and optimizing cover letters. 
      Your task is to generate five different angles or perspectives on how to enhance a cover letter to make it more impactful,
      clear, and relevant to a given job position. You are provided with the job advertisements tasks and requirements with the question. 
      Consider various aspects such as tone, structure, and alignment with the job requirements. Also, ensure these suggestions 
      are framed in a way that helps in retrieving relevant data from a vector database of excellent cover letters. Provide 
      these distinct improvement suggestions separated by newlines. <|eot_id|><|start_header_id|>user<|end_header_id|>

      Question: {question} \n <|eot_id|><|start_header_id|>assistant<|end_header_id|>""",
    )

    retriever = MultiQueryRetriever.from_llm(
        vectorstore.as_retriever(), 
        ollama,
        prompt=QUERY_PROMPT
    )

    template = """Answer the question based on the following context: {context}
    Question: {question}"""

    return retriever, ChatPromptTemplate.from_template(template)