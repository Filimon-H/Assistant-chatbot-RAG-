import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Set up Streamlit UI
st.title("🧠 Groq LLM Chatbot")

# Input from user
user_input = st.text_input("Ask a question about ML, AI, or anything else:")

# LLM Initialization
llm = ChatGroq(
    model="llama3-8b-8192",  # or "llama-3.1-8b-instant"
    temperature=0.7,
    api_key=api_key
)

# Handle query
if user_input:
    with st.spinner("Thinking..."):
        messages = [
            SystemMessage(content="You are a helpful AI assistant."),
            HumanMessage(content=user_input)
        ]
        response = llm.invoke(messages)
        st.success("Answer:")
        st.markdown(response.content)
