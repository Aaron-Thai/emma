import streamlit as st
import nltk
import random
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

# Streamlit app
st.markdown("<h1 style='text-align: center;'>Emma</h1>", unsafe_allow_html=True)
col = st.columns([4, 4, 4])
with col[1]:
    st.image("emma2.jpg", width=200)

# Output container
output_container = st.container()
output_placeholder = output_container.empty()

# Initialize session_state for output if not already set
if "emma_output" not in st.session_state:
    st.session_state.emma_output = "Output will appear here..."

output_placeholder.markdown(
    f"<div style='background-color: #f0f0f0; padding: 10px; border: 1px solid #ddd; min-height: 50px;'>{st.session_state.emma_output}</div>",
    unsafe_allow_html=True
)

st.write("")  # spacing
st.write("")

search_string = st.text_input("Message:")

enter_clicked = st.button("Enter")

if enter_clicked:
    if search_string.strip():
        with st.spinner('Thinking...'):
            result = get_emma_response(search_string)  # Using the updated function
        st.session_state.emma_output = result
    else:
        st.warning("Please enter a part of a sentence to search.")

# Always update the output
output_placeholder.markdown(
    f"<div style='background-color: #f0f0f0; padding: 10px; border: 1px solid #ddd; min-height: 50px;'>{st.session_state.emma_output}</div>",
    unsafe_allow_html=True
)
