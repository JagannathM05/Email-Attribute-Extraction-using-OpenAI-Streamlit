import streamlit as st
import os
import sqlite3
import openai
from openai import OpenAI

# Set your OpenAI API key here
os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"
max_tokens = 512

def gen_response(input):

  client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
  )

  chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": input,
        }
    ],
    model="gpt-3.5-turbo",
  )

  response = chat_completion.choices[0].message.content

  return response

prompt = """
Extract the following attributes from the given e-commerce product complaint email thread:
1. Product name or description
2. Issue description (eg: damaged, missing, etc.)
3. Order number (if available)
4. Resoultion steps or actions (if mentioned)
5. Issue raised Date and Time
6. Complaint Email ID
7. Complaint Name
8. Number of emails in the thread

Provide the output in JSON format

Email Thread: 

"""

st.set_page_config(page_title ="Attribute Extraction")

st.header("Email Attribute Extraction")

uploaded_file = st.file_uploader("Choose a text file", type ="txt")
 
submit = st.button("Submit")

if uploaded_file is not None:
  email_thread = uploaded_file.read().decode("utf-8")

if submit:
  input = prompt + email_thread
  response = gen_response(input)
  st.subheader("Response: ")
  st.write(response)