# Emma
Chat with Jane Austen's Emma, try it here: https://emma-ai.streamlit.app/

# Introduction
Conversational AI like ChatGPT has come under fire from the NYT for copyright infringement.  
What if there was an AI platform trained only on public domain, opt-in, or CC0 data?  

# Methods
To start, let's use Jane Austen's Emma, published in 1815.  
It's in the public domain via Project Gutenberg, and accessible via the NLTK corpus.  

Let's also use an image generation model trained only on public domain images.  
See the huggingface for Mitsua Diffusion One here: https://huggingface.co/Mitsua/mitsua-diffusion-one  
Try the demo here: https://huggingface.co/spaces/Mitsua/Likes-demo   

For the character image, I tried this prompt from ChatGPT, with the Guidance Scale around 4:  

"Anime-style portrait of Emma Woodhouse,   
beautiful young woman, long brown hair, wearing a delicate empire-waist gown with lace and soft pastel colors.   
She stands in an English garden, with a confident, playful smile.   
Soft lighting, detailed background, romantic and classic anime art style."  

Meta.AI was prompted to provide code for the webapp, and it chose to use Streamlit not me. :)
ChatGPT was later used to add more functionality and fixes.

# Results
Prompting: enter any text using a word from the book  
Model: will find the first sentence with your word  
Output: receive it or the next sentence after that  

# Discussion
Obviously this will only work with the words in the book that were available in 1815.  
I have tried to include a vocabulary list on the side, but it slows the page significantly.

Standard features to borrow from Character AI include chat history, expanded training data, and more varied answers.  
NLP to read user prompts, detect the most relevant keyword, and do sentiment analysis would also be interesting.  
But first, being able to prompt with a full sentence is probably the priority for natural interaction.
