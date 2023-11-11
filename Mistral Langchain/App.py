import streamlit as st 
# LLM
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = Ollama(
    model="mistral:7b-instruct",
    verbose=True,
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
)

st.write("Mistral WebAPP")

prompt = st.text_input("Enter prompt")

st.write(llm(prompt))
