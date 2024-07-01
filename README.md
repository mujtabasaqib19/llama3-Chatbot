# README for Chatbot powered by llama3

## Overview

This project creates a chatbot using the `llama3` language model from the Langchain Community library and a Streamlit-based user interface. Users can interact with the chatbot by entering queries, and the chatbot generates responses using the `llama3` model.

## Features

- **Interactive Chat Interface:** Users can type questions and receive responses from the `llama3` model.
- **Real-time Response Generation:** The application provides real-time feedback while generating responses.
- **Error Handling:** The application handles errors gracefully and provides feedback in case of issues.

## Requirements

- Python 3.8 or higher
- Streamlit
- Langchain Community library (`llms` package)

## Installation

1. **Clone the repository:**

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```sh
   pip install streamlit langchain_community
   ```

## Usage

1. **Run the Streamlit app:**

   ```sh
   streamlit run app.py
   ```

2. **Interact with the Chatbot:**

   - Open your web browser and go to the local URL provided by Streamlit.
   - Type your question into the text area.
   - Click the "Generate" button to get a response.

## Code Explanation

### Initialization

```python
from langchain_community.llms import Ollama
import streamlit as st

# Initialize the LLM
llm = Ollama(model="llama3")
```

The language model `llama3` from the Langchain Community library is initialized.

### Model Invocation

```python
def invoke_model(query):
    try:
        # Assuming 'invoke' is the correct method name and requires parameters like 'inputs'
        response = llm.invoke(inputs=query)
        return response
    except Exception as e:
        return f"An error occurred: {str(e)}"
```

This function sends a query to the model and returns the generated response. It also handles any potential errors.

### Streamlit UI Setup

```python
# Setting up the Streamlit UI
st.title("Chatbot powered by llama3")

message = st.text_area("Ask any Question")

if st.button("Generate"):
    if message:
        with st.spinner("Generating response..."):
            response = llm.stream(message, stop = [''])
            st.write(response)
```

The Streamlit interface includes:

- A title for the application.
- A text area for users to input their queries.
- A button to generate responses.
- A spinner to indicate that a response is being generated.


Thank you for using our Chatbot powered by llama3! We hope you find it useful and engaging. If you have any feedback or suggestions, feel free to reach out to us.
For any questions or inquiries, please contact me at mujtabasaqib654@gmail.com.
