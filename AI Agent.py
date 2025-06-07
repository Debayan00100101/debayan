import streamlit as st
import google.generativeai as genai

# Configure Streamlit page
st.set_page_config("Gemini", page_icon="🧠")
st.title("🧠 AI Agent")

# Configure Gemini API key
genai.configure(api_key="AIzaSyCFdHMPJiR7hotEWC0tQqTR2cxl1qf6veE")
model = genai.GenerativeModel("gemini-2.0-flash")

# Initialize chat history in session state
if "chat" not in st.session_state:
    st.session_state.chat = []

# Display chat messages
for user_msg, bot_msg in st.session_state.chat:
    st.success(user_msg, icon="😀")  # User message in green
    st.info(bot_msg, icon="🧠")      # Bot message in blue

# Input text box and send button in columns
col1, col2 = st.columns([8, 1])
with col1:
    user_input = st.text_input(
        "Type your message",
        placeholder="Type Here...",
        label_visibility="collapsed",
        key="user_input"
    )
with col2:
    send = st.button("⩥")

# Handle send button click
if send and user_input.strip():
    with st.spinner("Thinking..."):
        try:
            response = model.generate_content(user_input)
            answer = response.text
        except Exception as e:
            answer = f"Error: {e}"

    # Append new conversation pair to chat history
    st.session_state.chat.append((user_input, answer))

    # Clear input after sending
    st.user_input = ""
    st.rerun()