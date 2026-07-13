from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv
import streamlit as st

load_dotenv()



model = ChatAnthropic(model="claude-opus-4-8")

st.header("Research Tool")

# We are requiring an input from the user to select a research paper, explanation style and length of the summary.
paper_input = st.selectbox("Select a research paper", ["Select...", "Attention is all you need", "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])
style_input = st.selectbox("Select Explanation Style", ["Begginer-Friendly", "Technical", "Code-Oriented", "Mathematical"])
length_input = st.selectbox("Select Explanation Length", ["Short(1-2 aparagraphs)", "Medium(3-5 paragraphs)", "Long(detailed explanation)"])


template = load_prompt("template.json")

#fill the placeholders based on the user input and generate the prompt for the model. The filled prompt is then passed to the model for generating the summary.
"""prompt = template.invoke({
    "paper_input":paper_input,
    "style_input":style_input,
    "length_input":length_input
})"""

if st.button("Summarize"):
    chain = template | model
    result = chain.invoke({
    "paper_input":paper_input,
    "style_input":style_input,
    "length_input":length_input
})
    st.write(result.content)