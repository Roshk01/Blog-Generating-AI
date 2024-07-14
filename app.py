import os
import google.generativeai as genai
from appapikey import google_gemini_api_key,openai_api_key
import streamlit as st

genai.configure(api_key=google_gemini_api_key)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

st.set_page_config(layout='wide')
st.title("Blog Post Writing AI")
st.subheader('Generate Your Blog Content within a second using AI.')

with st.sidebar:
    st.title('Blog Details')
    st.subheader("FillOut the Blog Details You Want to Generate")
    blog_title = st.text_input('Blog Title')

    blog_keywords = st.text_area('Keywords(Saperated with commas)')
    num_len = st.slider("Length of Words", min_value=250, max_value= 1000, step=250)
    # pic_len = st.number_input("Number Of Images",min_value=1, max_value=5, step=1)

    input_promt = [f"generate a comprehensive blog post in the given title \"{blog_title}\" and by using keywords {blog_keywords}. the blog should be in {num_len} word length. it should be suitable for the online viewers, maintain it's tone , original content , and informative."]

    response = model.generate_content(input_promt)
    # Submit Button 
    submit_button = st.button('Generate Blog')



if submit_button:
    st.write(response.text)