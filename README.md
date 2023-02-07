# GPT Semantic Search

## Introduction

GPT Semantic Search is a tool that uses OpenAI's GPT-3 to perform semantic search on text documents. Given a set of text documents, the tool will summarize each document and allow the user to ask questions about the summarized information. The answers are generated using OpenAI's GPT-3 language model.

![](https://github.com/ErnestAroozoo/GPT-Semantic-Search/blob/master/GPT%20Semantic%20Search.png)

## Getting Started

1. Install the necessary dependencies: `streamlit`, `openai`, and `python-dotenv`.

2. Clone the repository and create a `.env` file in the project directory to store your OpenAI API key.

3. Run the application using `streamlit run main.py`.

## Usage

1. Input the text you want to search by providing the required information in the provided text area.

2. The tool will summarize each section of the text into multiple short point forms.

3. The summarized information will then be displayed.

4. You can then ask questions about the summarized information by entering it into the provided text input.

## Note

This tool may consume a large number of tokens when processing lengthy documents. To avoid this, it is advisable to modify the code to utilize the smaller GPT models instead of the default davinci-003 model for document summarization.

