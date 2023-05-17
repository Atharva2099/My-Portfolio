#Dependencies
import os
from apikey import apikey

import streamlit as st
from langchain import PromptTemplate, HuggingFaceHub, LLMChain

os.environ['HUGGINGFACEHUB_API_TOKEN'] = apikey


#APP framework
st.title('HuGGinGFacE langchain model')
prompt = st.text_input(' plug in your prompt')


#LLm
llm=HuggingFaceHub(repo_id="bigscience/bloom", model_kwargs={"temperature":1e-10})


if prompt:
    response = llm(prompt)
    st.write(response)
