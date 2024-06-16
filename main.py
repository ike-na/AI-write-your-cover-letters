from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from utilities import get_chunks, get_retriever, get_vectorstore



def main():
  ollama = Ollama(model="llama3")
  chunks = get_chunks("training/combined.pdf")
  vectorstore = get_vectorstore(chunks)

  retriever, prompt = get_retriever(vectorstore, ollama)

  chain = (
      {"context": retriever, "question": RunnablePassthrough()}
      | prompt
      | ollama
      | StrOutputParser()
  )

  requirements_list = []
  while True:
      requirement = input("Enter a job task or requirement (or type 'f' to finish): \n")
      if requirement.lower() == 'f':
          break
      requirements_list.append(requirement.strip())

  formatted_requirements = ", ".join(requirements_list)
  print("\nFixing the OllamaEmbeddings and writing the cover letter...\n")

  result = chain.invoke({"question": f"Can you write me a 200-300 word cover letter to the unnamed position [position] at unnamed company [company]. Make sure that the requirements are answered in bullet points. The requirements are: {formatted_requirements}?"})
  print(result)

  # vectorstore.delete_collection() # Uncomment this line to delete the vectorstore



if __name__ == "__main__":
    main()