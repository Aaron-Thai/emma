# Fastest version of Emma, Streamlit-ready

import streamlit as st
import nltk
from nltk.tokenize import sent_tokenize

# Load Emma text from a local file
with open('emma.txt', 'r', encoding='utf-8') as file:
    emma_text = file.read()

# Split the text into sentences
sentences = sent_tokenize(emma_text)

def get_next_sentence(search_string):
    search_string = search_string.lower()
    for i, s in enumerate(sentences):
        if search_string in s.lower():
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
output_placeholder.markdown(
    "<div style='background-color: #f0f0f0; padding: 10px; border: 1px solid #ddd; min-height: 50px;'>Output will appear here...</div>",
    unsafe_allow_html=True
)

st.write("")  # Add some spacing
st.write("")

search_string = st.text_input("Message:")

if st.button("Enter"):
    with st.spinner('Thinking...'):
        result = get_next_sentence(search_string)
    output_placeholder.markdown(
        f"<div style='background-color: #f0f0f0; padding: 10px; border: 1px solid #ddd; min-height: 50px;'>{result}</div>",
        unsafe_allow_html=True
    )
