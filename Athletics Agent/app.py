import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever  # this loads your Chroma retriever

st.set_page_config(page_title="Athletics Rankings Chatbot", layout="wide")

st.title("Athletics Rankings Chatbot")

model = OllamaLLM(model="llama3.2")

template = """
You are an elite athletics data analyst.

Using the provided competition records, answer historical and statistical questions clearly, citing athlete names, countries, rankings, and marks where possible.

Context:
{reviews}

Question:
{question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Streamlit chat interface
question = st.text_input("Ask about athletics rankings:")

if question:
    with st.spinner("Retrieving relevant records..."):

        docs = retriever.invoke(question)


        response = chain.invoke({"reviews": docs, "question": question})


        st.subheader("Chatbot Answer")

        st.write(response)


        with st.expander("Top 5 Relevant Records"):
            for i, doc in enumerate(docs):
                st.markdown(f"**Result {i+1}**")
                st.write(doc.page_content)
      
      
      
  
  

  
  

  
  