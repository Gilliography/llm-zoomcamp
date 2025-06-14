from ast import While
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


model = OllamaLLM(model="Llama3.2")

template = """
You are an expert in answering questions about a Pizza Restaurant
here are some relevant reviews: {reviews}

Here is the question to answer: {question}

"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


while True:
    question = input("Enter your question about the pizza restaurant (q to quit): ")
    if question.lower() == "q":
        break
    result = chain.invoke({"reviews": [], "question": question})
    print(result)
