# test version of Emma chatbot using Streamlit
# features added: conversation history, clear chat button, and improved UI

import streamlit as st
import nltk
import random
import time
from nltk.tokenize import sent_tokenize

# Only download 'punkt' once
nltk.download('punkt', quiet=True)

# Cache loading the book
@st.cache_data
def load_emma_text():
    with open('emma.txt', 'r', encoding='utf-8') as file:
        return file.read()

emma_text = load_emma_text()
sentences = sent_tokenize(emma_text)
sentences = [s.replace('\n', ' ') for s in sentences]  # remove line break character

def get_emma_response(user_input):
    user_input = user_input.lower()
    matching_sentences = [
        s for s in sentences if any(word in s.lower() for word in user_input.split())
    ]

    if matching_sentences:
        return random.choice(matching_sentences)
    else:
        fallback_replies = [
            "I cannot always comprehend others, but I always have a ready smile.",
            "Surely you must know I am not without resource, even in perplexity.",
            "If I cannot find the words, I shall simply dazzle instead.",
            "Your message puzzles me, but I shall pretend otherwise!"
        ]
        return random.choice(fallback_replies)

# Initialize conversation history
if "conversation" not in st.session_state:
    st.session_state.conversation = []  # list of (speaker, message) pairs

# Streamlit app layout
st.markdown("<h1 style='text-align: center;'>Emma</h1>", unsafe_allow_html=True)
col = st.columns([4, 4, 4])
with col[1]:
    st.image("emma2.jpg", width=200)

st.write("")  # spacing

# 👉 Display conversation history first, above the input box
st.markdown("<h3>Conversation</h3>", unsafe_allow_html=True)
for speaker, message in st.session_state.conversation:
    if speaker == "You":
        st.markdown(f"<div style='background-color: #dceefc; padding: 8px; border-radius: 10px; margin-bottom: 5px;'><strong>You:</strong> {message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='background-color: #f0f0f0; padding: 8px; border-radius: 10px; margin-bottom: 10px;'><strong>Emma:</strong> {message}</div>", unsafe_allow_html=True)

st.write("")  # spacing

# 👉 Input box and buttons below the conversation history
search_string = st.text_input("Message:")

col1, col2, col3 = st.columns([4, 1, 1])
enter_clicked = col1.button("Enter")
clear_clicked = col3.button("Clear Chat")

if clear_clicked:
    st.session_state.conversation = []
    st.success("Chat cleared!")
    st.rerun()  # Forces the script to rerun and clears the chat history instantly

if enter_clicked:
    if search_string.strip():
        with st.spinner("Emma is thinking..."):
            time.sleep(1)
            result = get_emma_response(search_string)
        # Add to conversation history
        st.session_state.conversation.append(("You", search_string))
        st.session_state.conversation.append(("Emma", result))
        # Keep only the last 2 entries (1 round)
        st.session_state.conversation = st.session_state.conversation[-2:]
    else:
        st.warning("Please enter a message.")
    
    # Ensure the updated conversation appears right after the Enter button click
    st.rerun()  # Forces the script to rerun, which updates the conversation display
