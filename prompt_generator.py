from langchain_core.prompts import PromptTemplate

#Template for the prompt based on the user input. The template includes placeholders for the research paper title, explanation style, and explanation length. It also specifies that the summary should include mathematical details and analogies, and instructs the model to respond with "Insufficient information available" if certain information is not present in the paper.
template = PromptTemplate(
    template="""
    Please summarize the research paper titled "{paper_input}" with the following specifications:
    Explanation Style: {style_input}
    Explanation Length: {length_input}
    1. Mathematical Details: 
        - Include relevant mathematical equations if present in the paper.
        - Explain the mathematical concepts using using simple intuitive code snippets where applicable.
    2. Analogies: 
        - Use relatable analogies to simplify complex concepts.
    If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
    Ensure the summmary is clear, accurate and aligned with the provided style and length.
    """,
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True
)

template.save("template.json")

