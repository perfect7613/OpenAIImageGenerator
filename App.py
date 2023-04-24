import streamlit as st
from Apikey import OPENAI_API_KEY
import openai
import urllib.request
from PIL import Image


openai.api_key = OPENAI_API_KEY

def generate_image(image_desc):
    response = openai.Image.create(
        prompt = image_desc,
        n = 1,
        size = "512x512",
    )

    img_url = response['data'][0]['url']

    urllib.request.urlretrieve(img_url, "image.png")

    image = Image.open("image.png")

    return image

def generate_image_suggestions():
    suggestions = openai.Completion.create(
        model = "text-davinci-003",
        prompt = "Give Image Suggestions for the DALLE Image Generator",
        temperature = 0.9,
        max_tokens = 500,
    )


    suggestion = suggestions.choices[0].text.strip()

    return suggestion





st.title("Image Generator Web App")
text_input = st.text_input("Enter a prompt to generate an image:")

if st.button("Generate Image"):
    final_output = generate_image(text_input)
    st.image(final_output)

if st.button("Get Image Suggestions"):
    suggestion = generate_image_suggestions()
    st.write(suggestion)

    

