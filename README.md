# 🔎 AI Research Assistant with LangChain + Groq

This project is an AI-powered Research Assistant built using **LangChain Agents**, **Groq (Llama 3)**, and **Streamlit**.  
It can intelligently search the web, retrieve Wikipedia information, and fetch Arxiv research papers in real time using an autonomous ReAct agent.

---

## 🧠 How It Works

1. The user enters a question in the Streamlit chat interface.
2. The query is passed to a **LangChain ReAct Agent**.
3. The agent uses **Groq’s Llama 3 model** to reason about the query.
4. Based on the question, the agent decides which tool to use:
   - 🌐 DuckDuckGo (Web Search)
   - 📚 Wikipedia API
   - 🧪 Arxiv API
5. The selected tool retrieves relevant information.
6. The LLM processes the tool output and generates a final response.
7. The response is streamed back to the user in real time.

---

## 🛠 Technologies Used

- **LangChain** – Agent framework & tool orchestration  
- **Groq API** – Fast Llama 3 inference  
- **Streamlit** – Interactive chat UI  
- **DuckDuckGo Search** – Real-time web search  
- **Wikipedia API** – Structured knowledge retrieval  
- **Arxiv API** – Research paper access  
- **Python & dotenv** – Backend & environment management  

---

## 🚀 Key Features

- ReAct-based autonomous agent reasoning
- Real-time external knowledge retrieval
- Streaming responses
- Clean and interactive chat interface
- Secure API key handling using `.env`

---

## 🎥 Demo

Add your screen recording here for better visibility:

## Run Locally:-
- git clone https://github.com/your-username/your-repo-name.git
- cd your-repo-name
- pip install -r requirements.txt
- streamlit run app.py

## Deployed in Streamlit :-
check out the link here :- 
https://search-engine-gen-ai-app-using-tool-agent-kbrz9dsdcs56nruhpuaw.streamlit.app/

```markdown
## 🎬 Application Glimpse

![Demo](<img width="960" height="409" alt="image" src="https://github.com/user-attachments/assets/72e3ace3-00fe-4fe0-b340-9b0fc7772233" />
)

