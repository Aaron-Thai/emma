import streamlit as st
import nltk
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

search_string = st.text_input("Enter part of a sentence:")

enter_clicked = st.button("Enter")

if enter_clicked:
    if search_string.strip():
        with st.spinner('Thinking...'):
            result = get_next_sentence(search_string)
        st.session_state.emma_output = result
    else:
        st.warning("Please enter a part of a sentence to search.")

# Always update the output
output_placeholder.markdown(
    f"<div style='background-color: #f0f0f0; padding: 10px; border: 1px solid #ddd; min-height: 50px;'>{st.session_state.emma_output}</div>",
    unsafe_allow_html=True
)
