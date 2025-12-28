**🤖 GenAI Chatbot**

A **Generative AI** chatbot built with **LangChain + Python**, deployed using **Streamlit**, and powered by the** GROQ LLM **for ultra-fast inference.
This project demonstrates how to build a stateful conversational AI system with memory, role-based messages, and persistent chat history. 

**🚀 Features**
* 🔗 LangChain-based LLM orchestration
* ⚡ GROQ LLM integration for low-latency responses
* 🧠 Persistent chat memory using Streamlit session state
* 👥 Role-based conversations (User ↔ Assistant)
* 🌐 Streamlit UI for real-time interaction

**🛠️ Tech Stack**
* LLM <-> GROQ
* Framework <-> LangChain
* Python
* Streamlit

**💡 Key Concepts & Code Design**

**1️⃣ Role-Based Chat System**

The chatbot uses structured messages with explicit roles (user, assistant) to maintain conversational context. 
_st.session_state.chat_message = [
    {"role": "user", "content": user_input},
    {"role": "assistant", "content": response}
]_

**2️⃣ Persistent Chat Memory**

To simulate “memory,” the chatbot stores all previous exchanges using:
__st.session_state.chat_history.append(
    {"role": "user", "content": user_input}
)_ & 
_st.session_state.chat_history.append(
    {"role": "assistant", "content": response}
)_

This program prevents the chatbot from “forgetting” earlier messages and enables contextual follow-up questions. 

**3️⃣ Streamlit Session State Management**

Streamlit reruns the script on every interaction. Without _st.session_state_, chat history would reset on every user input. 

_if "chat_history" not in st.session_state:
    st.session_state.chat_history = []_

**▶️ Running the Project**

_git clone https://github.com/g-diasha/genai-chatbot.git_

_cd genai-chatbot_

_pip install -r requirements.txt_

_streamlit run app.py_

**🔐 Environment Variables**
A .env file is created to protect the GROQ API KEY. 

_GROQ_API_KEY=my_api_key_here_


















