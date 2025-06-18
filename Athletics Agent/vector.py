from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import pandas as pd
import os

# Load the dataset
df = pd.read_csv("data/world-athletics_all-time-top-lists.csv")

# Initialize the embeddings model
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Setup Chroma DB path
db_location = "athletics_chroma_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        content = (
            f"{row['competitor']} from {row['nat']} ranked #{row['event_rank']} in {row['event']} "
            f"with a mark of {row['mark']} at {row['venue']} on {row['date']}. "
            f"Gender: {row['gender']}, Age Category: {row['age_category']}, Environment: {row['environment']}."
        )

        metadata = {
            "event": row['event'],
            "mark": row['mark'],
            "rank": row['event_rank'],
            "date": row['date'],
            "venue": row['venue'],
            "gender": row['gender'],
            "category": row['age_category']
        }

        doc = Document(page_content=content, metadata=metadata, id=str(i))
        documents.append(doc)
        ids.append(str(i))

# Create or load vector store
vector_store = Chroma(
    collection_name="athletics_rankings",
    embedding_function=embeddings,
    persist_directory=db_location,
)

# Populate the vector store
if add_documents:
    vector_store.add_documents(documents, ids=ids)
    vector_store.persist()

# Create retriever (always available)
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5},
)
