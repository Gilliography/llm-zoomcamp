# 🏃‍♂️ Athletics AI Chatbot – LLM Zoomcamp Project

This project is part of my learning journey in the **LLM Zoomcamp**. The goal was to build an AI chatbot capable of answering questions about athletics using historical world records data from Kaggle. The chatbot is powered by **LangChain**, **Ollama**, and **ChromaDB**, and features a simple **Streamlit** UI for user interaction.

---

## 📌 Features

- 🔍 Search and ask questions about athletics records and athletes
- 🧠 Uses vector search for semantic understanding
- 📂 Processes data from a Kaggle CSV file
- 🖥️ Local language model inference via Ollama
- 🧩 Built with LangChain and ChromaDB
- 🎨 Interactive UI via Streamlit

---

## 🗂️ Project Structure

```

Athletics-Agent/
├── main.py                 # Streamlit app interface
├── vector.py              # Data ingestion, vector store creation
├── requirements.txt       # Python dependencies
├── data/
│   └── world-athletics\_all-time-top-lists.csv
└── README.md              # This file

````

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/athletics-agent.git
cd athletics-agent
````

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Qdrant with Docker

```bash
docker pull qdrant/qdrant
docker run -p 6333:6333 -p 6334:6334 \
   -v "$(pwd)/qdrant_storage:/qdrant/storage:z" \
   qdrant/qdrant
```

### 5. Run the App

```bash
streamlit run main.py
```

---

## 📦 Requirements

```txt
langchain
langchain-core
langchain-community
langchain-ollama
pandas
chromadb
streamlit
```

---

## 💡 Technologies Used

* [LangChain](https://www.langchain.com/)
* [Ollama](https://ollama.com/) – Local LLM hosting
* [ChromaDB](https://www.trychroma.com/) – Vector database
* [Streamlit](https://streamlit.io/) – UI framework
* [Pandas](https://pandas.pydata.org/) – Data processing
* [Qdrant](https://qdrant.tech/) – Vector similarity engine

---

## 📈 Future Improvements

* [ ] Add model selection options (e.g., switch between GPT-4, LLaMA, etc.)
* [ ] Support follow-up questions (conversation memory)
* [ ] Deploy the app on Hugging Face Spaces or Streamlit Cloud
* [ ] Add filters for athlete name, event, or year

---

## 🙋‍♂️ Author

**Gilbert Kiprotich**
Follow my [LLM Zoomcamp journey](https://twitter.com/yourhandle) and stay tuned for more updates!

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for details.

```

---

Would you like me to generate a GitHub-style project thumbnail, deploy instructions, or a badge set for this README?
```
