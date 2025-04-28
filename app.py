# fastest version of emma for now, idk why the other one lags

import streamlit as st
import nltk

# Download required NLTK data if not already downloaded
try:
    nltk.data.find('corpora/gutenberg')
except LookupError:
    nltk.download('gutenberg')

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

from nltk.tokenize import sent_tokenize

# Get the text from the NLTK corpus
emma_text = nltk.corpus.gutenberg.raw('austen-emma.txt')

# Split the text into sentences
sentences = sent_tokenize(emma_text)

def get_next_sentence(search_string):
    for i, s in enumerate(sentences):
        if search_string in s:
            if i < len(sentences) - 1:
                return sentences[i + 1]
            else:
                return "This is the last sentence in the book."
    return "Sentence not found in the book."

# Streamlit app
st.markdown("<h1 style='text-align: center;'>Emma</h1>", unsafe_allow_html=True)
col = st.columns([4, 4, 4])
with col[1]:
    st.image("emma2.jpg", width=200)

# Create a container with a placeholder background
output_container = st.container()
output_placeholder = output_container.empty()
output_placeholder.markdown("<div style='background-color: #f0f0f0; padding: 10px; border: 1px solid #ddd; min-height: 50px;'>Output will appear here...</div>", unsafe_allow_html=True)

st.write("")  # Add an empty line
st.write("")  # Add another empty line

search_string = st.text_input("Message:")

if st.button("Enter"):
    result = get_next_sentence(search_string)
    output_placeholder.markdown(f"<div style='background-color: #f0f0f0; padding: 10px; border: 1px solid #ddd; min-height: 50px;'>{result}</div>", unsafe_allow_html=True)