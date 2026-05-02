import streamlit as st
from app.chains import get_chain

# Initialize chain
chain = get_chain()

#PAge Title
st.set_page_config(page_title="Tech Chatbot", page_icon="🧑‍💻")

st.title("🧑‍💻⚡ Gaurav - Tech Chatbot")
st.write("Ask only tech-related questions to Gaurav.")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask your tech question...")

if user_input:
    # Add message to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(user_input)

    # Get response from chain
    response = chain.invoke({"input": user_input})

    # Add bot response to history
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant", avatar="🧠"):
        st.markdown(response)