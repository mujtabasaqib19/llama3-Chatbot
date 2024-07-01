from langchain_community.llms import Ollama
import streamlit as st

# Initialize the LLM
llm = Ollama(model="llama3")

def invoke_model(query):
    try:
        # Assuming 'invoke' is the correct method name and requires parameters like 'inputs'
        response = llm.invoke(inputs=query)
        return response
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Setting up the Streamlit UI
st.title("Chatbot powered by llama3")

message = st.text_area("Ask any Question")

if st.button("Generate"):
    if message:
        with st.spinner("Generating response..."):
            response = llm.stream(message, stop = ['<|eot_id|>'])
            st.write(response)
