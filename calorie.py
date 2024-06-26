import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

api_key='Your Gemini pro api_key'
genai.configure(api_key=api_key)

def get_gemini_repsonse(input_prompt,image,input):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input_prompt,image[0]])
    return response.text


def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")




st.set_page_config(page_title='Calories Advisor APP')
st.header('Calories Advisor APP')
uploaded_file=st.file_uploader("Choose an image..",type=["jpg","jpeg","png"])
image=''
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image...",use_column_width=True)
submit=st.button("Tell me about the Food")



input_prompt="""
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format
                if any of calories,crbohydrates,vitamins,fats and proteins have 0grams  then dont include in the out else
                include in the output
               1. name of Item 1 - no of calories, no of crbohydrates, no of vitamins, no of fats,and no of proteins
               2. name of Item 2 - no of calories, no of crbohydrates, no of vitamins, no of fats,and no of proteins
                        
               ----
               ----
at last tell me whether the food ids good for health or not based on calories,carbohydrates and fats and vitamins.

"""

## If submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)
