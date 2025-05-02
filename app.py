import streamlit as st
import random
import nltk
from nltk.tokenize import sent_tokenize

# Download punkt once
nltk.download('punkt', quiet=True)

import re

# Cache loading and cleaning the book
@st.cache_data
def load_emma_text():
    with open('emma.txt', 'r', encoding='utf-8') as file:
        raw_text = file.read()
    
    # Remove lines like "VOLUME I", "CHAPTER I", etc.
    cleaned_text = re.sub(r'(VOLUME\s+[IVX]+|CHAPTER\s+[IVX]+)', '', raw_text, flags=re.IGNORECASE)
    
    return cleaned_text

emma_text = load_emma_text()
sentences = sent_tokenize(emma_text)
sentences = [s.replace('\n', ' ') for s in sentences]  # Remove line break character

# Function for matching based on user input
def get_emma_response(user_input, exact_match):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    if exact_match:
        # Look for exact match of the input phrase in the sentences
        matching_sentences = [
            s for s in sentences if user_input in s.lower()
        ]
    else:
        # Look for any word in the sentence
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

# Streamlit app layout
st.markdown("<h1 style='text-align: center;'>Emma</h1>", unsafe_allow_html=True)
col = st.columns([4, 4, 4])
with col[1]:
    st.image("emma2.jpg", width=200)

# Output container (moved above message input)
output_container = st.container()
output_placeholder = output_container.empty()

# Initialize session_state for output if not already set
if "emma_output" not in st.session_state:
    st.session_state.emma_output = "Output will appear here..."

# Always update the output
output_placeholder.markdown(
    f"<div style='background-color: #f0f0f0; padding: 10px; border: 1px solid #ddd; min-height: 50px;'>{st.session_state.emma_output}</div>",
    unsafe_allow_html=True
)

st.write("")  # spacing
st.write("")  # spacing

# Input box
search_string = st.text_input("Message:")

# Create a layout with columns for Enter button and checkbox
col1, col2 = st.columns([4, 1])

with col1:
    enter_clicked = st.button("Enter")

with col2:
    # Place the checkbox to the right in the second column
    exact_match = st.checkbox("Exact Match", value=False)

# If Enter button is clicked, get the response
if enter_clicked:
    if search_string.strip():
        with st.spinner('Thinking...'):
            result = get_emma_response(search_string, exact_match)
        st.session_state.emma_output = result
    else:
        st.warning("Please enter a part of a sentence to search.")
    st.rerun()  # Forces the script to rerun and update the output instantly