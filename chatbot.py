from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st

load_dotenv()

st.set_page_config(
    page_title="ChatBot",
    page_icon="💬",
    layout="centered"
)
st.title("💭 Generative AI ChatBot")

#initiate chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


#show chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#initiate LLM
llm = ChatGroq(
    model ="llama-3.3-70b-versatile",
    temperature = 0.0,
)
#user query
user_prompt = st.chat_input("Ask me anything...")

#display user query and save the query to the chat history
if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user", "content":user_prompt})
    response = llm.invoke(
        input=[{"role":"system", "content": "You are a helpful AI assistant"}, *st.session_state.chat_history]
)
    ai_response = response.content
    st.session_state.chat_history.append({"role":"assistant", "content":ai_response})
    with st.chat_message("assistant"):
        st.markdown(ai_response)