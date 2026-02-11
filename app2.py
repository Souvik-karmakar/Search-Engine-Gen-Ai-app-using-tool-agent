import streamlit as st
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler


# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="LangChain Search Assistant",
    page_icon="🔎",
    layout="wide"
)

# -------------------- CUSTOM STYLING --------------------
st.markdown("""
    <style>
    .stChatMessage {
        border-radius: 12px;
        padding: 10px;
    }
    .block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- TITLE --------------------
st.title("🔎 AI Research Assistant")
st.caption("Powered by Groq + LangChain + Live Search Tools")

# -------------------- LOAD ENV --------------------
load_dotenv()

# -------------------- SIDEBAR --------------------
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input("Enter your Groq API Key", type="password")

    st.markdown("---")
    st.markdown("### 🛠 Tools Used")
    st.markdown("""
    - 🌐 DuckDuckGo Search  
    - 📚 Wikipedia  
    - 🧪 Arxiv Research Papers  
    """)

    st.markdown("---")
    st.info("This assistant can search the web and research papers in real-time.")

# -------------------- TOOLS SETUP --------------------
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=300)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=300)
wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)

search = DuckDuckGoSearchRun(name="Search")

tools = [search, arxiv, wiki]

# -------------------- SESSION STATE --------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 Hi! I can search the web, Wikipedia, and Arxiv papers. Ask me anything!"}
    ]

# -------------------- DISPLAY CHAT HISTORY --------------------
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# -------------------- USER INPUT --------------------
if prompt := st.chat_input("Ask me about AI, research papers, or anything..."):

    if not api_key:
        st.warning("⚠️ Please enter your Groq API key in the sidebar.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # LLM Setup
    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.3-70b-versatile",
        streaming=True
    )

    # Agent Setup
    search_agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handling_parsing_errors=True,
        verbose=True
    )

    # Assistant Response
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)

        response = search_agent.run(prompt, callbacks=[st_cb])

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
