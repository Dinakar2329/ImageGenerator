# Image Generator using OpenAI DALL-E API and Streamlit

![DALL-E Image Generator](https://your-image-generator-url.com/images/dalle_logo.png)

## Overview

Welcome to the Image Generator powered by OpenAI's DALL-E API and presented through Streamlit. This application allows you to generate high-quality images based on your textual input.

## Prerequisites

- Python 3.6+
- [Streamlit](https://streamlit.io/)
- [OpenAI Python Client](https://github.com/openai/openai-python)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/image-generator.git
   cd image-generator

1.Install dependencies:
   ```pip install streamlit openai```
2.Set up your OpenAI API key:

Replace ##"YOUR_API_KEY_HERE" 
with your actual OpenAI API key in the api_key field.

##Usage
1.Run the Streamlit app:
   ```python -m streamlit run app.py```
2.Enter a prompt in the input bar and click the "Generate Images" button.

Streamlit App Code
```
import streamlit as st
from openai import OpenAI

# API
api = OpenAI(api_key="YOUR_API_KEY_HERE")

# Function to Generate Image URLs
def Generate(user_input):
    response = api.images.generate(
        prompt=user_input,
        n=4,  # Generate 4 images
        size="1024x1024",
        quality="hd"
    )

    # Creating a list to store image URLs
    image_urls_list = []
    for image_data in response.data:
        image_url = image_data.url
        image_urls_list.append(image_url)

    # If no image URLs are generated
    if len(image_urls_list) == 0:
        raise ValueError("No images found in the API response.")

    return image_urls_list

# Streamlit UI
title = st.title("Image Generator")

container = st.container(border=True)
input_bar = st.text_input("Enter prompt to generate images")

button = st.button("Generate Images")
col1, col2, col3, col4 = st.columns(4)

# If button is clicked
if button or input_bar:
    try:
        image_urls1, image_urls2, image_urls3, image_urls4 = Generate(input_bar)
        col1.image(image_urls1, caption="Image 1")
        col2.image(image_urls2, caption="Image 2")
        col3.image(image_urls3, caption="Image 3")
        col4.image(image_urls4, caption="Image 4")
    except Exception as e:
        st.error(f"Error generating images: {e}") 
```
