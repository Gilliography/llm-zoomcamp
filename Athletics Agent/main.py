from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever  # this loads your Chroma retriever

# Load LLM from Ollama
model = OllamaLLM(model="llama3.2")

# Prompt template for athletics data
template = """
You are an elite athletics data analyst.

Using the provided competition records, answer historical and statistical questions clearly, citing athlete names, countries, rankings, and marks where possible.

Context:
{reviews}

Question:
{question}
"""

# Chain: prompt → model
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# CLI chat loop
while True:
    print("\n==============================")
    question = input("Ask about athletics rankings (or 'q' to quit): ")
    print("==============================\n")
    if question.lower() == "q":
        break

    # Retrieve relevant ranking records
    reviews = retriever.invoke(question)

    # Get model response
    result = chain.invoke({"reviews": reviews, "question": question})

    # Print the answer
    print(result)
