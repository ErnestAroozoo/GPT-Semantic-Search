import streamlit as st
import openai
import os
from dotenv import load_dotenv

# CUSTOMIZATION: Page configuration
st.set_page_config(
    page_title="GPT Semantic Search",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CUSTOMIZATION: Hide unnecessary UI elements
hide_streamlit_style = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
                .css-15zrgzn {display: none}
                #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# CUSTOMIZATION: Add custom footer
add_footer_style = """<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #212121;
color: #f1f1f1;
text-align: center;
padding: 2px;
font-size: 12px;
}
a {
color: #f1f1f1;
text-decoration: none;
}
</style>
<div class="footer">
<p>Made by <a href='https://github.com/ErnestAroozoo' target='_blank'>Ernest Aroozoo</a> | <a href='https://github.com/ErnestAroozoo/GPT-Semantic-Search' target='_blank'>View on GitHub</a></p>
</div>
"""
st.markdown(add_footer_style, unsafe_allow_html=True)

# OpenAI API Key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
# Title
st.title("🔍 GPT Semantic Search")
# Intro Text
intro = st.empty()
with intro.container():
    # Text body
    st.markdown("""
    ------------
    ### What is GPT Semantic Search?
    GPT Semantic Search is a tool that uses OpenAI's GPT-3 to perform semantic search on text documents. Given a set of text documents, the tool will summarize each document and allow the user to ask questions about the summarized information. The answers are generated using OpenAI's GPT-3 language model.

    """)
    st.info(
        'To get started, please provide the required information below.',
        icon="ℹ️")

# Step 1: Ask user to input the entire text
text = st.text_area("Provide the documents below:")

# Step 2: Split the text into sections
section_size = 2048
sections = [text[i:i+section_size] for i in range(0, len(text), section_size)]

# Step 3: Summarize each section
summaries = []
for section in sections:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize text as truthfully as possible by using only the text provided."
               f"Write it in a short and concise manner such that only important contexts and ideas preserved. "
               f"It should be written in point form note taking format."
               f"\n\n "
               f"Text:\n"
               f"{section}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).get("choices")[0].get("text")
    summaries.append(response)

# Step 4: Display all summaries
st.write("Summaries:")
for summary in summaries:
    st.write(summary + "\n")

# Step 5: Pass all summaries to Q&A prompt
question = st.text_input("Ask a question:")
if text:
    if question:
        answer = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Answer the question as truthfully as possible using only the provided summary of the readings, "
                   f"and if the answer is not contained within the summary below, you must say 'I don't know'."
                   f"\n\n"
                   f"Summary:\n"
                   f"{' '.join(summaries)}\n\n"
                   f"Q: {question}\n\n"
                   f"A: ",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0,
        ).get("choices")[0].get("text")

        # Display answer
        st.write("Answer: " + answer)

# CUSTOMIZATION: Change footer again to prevent clipping
add_footer_style2 = """<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #212121;
color: #f1f1f1;
text-align: center;
padding: 2px;
font-size: 12px;
}
a {
color: #f1f1f1;
text-decoration: none;
}
</style>
<div class="footer">
<p>Made by <a href='https://github.com/ErnestAroozoo' target='_blank'>Ernest Aroozoo</a> | <a href='https://github.com/ErnestAroozoo/GPT-Semantic-Search' target='_blank'>View on GitHub</a></p>
</div>
"""
st.markdown(add_footer_style2, unsafe_allow_html=True)
