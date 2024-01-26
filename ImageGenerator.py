import streamlit as st
from openai import OpenAI

# API
api= OpenAI( api_key="")

# Function to Generate Image Urls
def Generate(user_input):
    response = api.images.generate(
        prompt=user_input,
        n=4,  #Generate 4 images
        size= "1024x1024",
        quality="hd"
    )
# Creating a list to store image urls
    image_urls_list = []
    for image_data in response.data:
        image_url = image_data.url
        image_urls_list.append(image_url)

# If no image urls are generated 
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
    with st.spinner("Generating Images..."):
        # Use empty() to create a placeholder for the images
        image_placeholder1 = col1.empty()
        image_placeholder2 = col2.empty()
        image_placeholder3 = col3.empty()
        image_placeholder4 = col4.empty()

        try:
            image_urls1, image_urls2, image_urls3, image_urls4 = Generate(input_bar)
            # Update the placeholders with the generated images
            image_placeholder1.image(image_urls1, caption="Image 1")
            image_placeholder2.image(image_urls2, caption="Image 2")
            image_placeholder3.image(image_urls3, caption="Image 3")
            image_placeholder4.image(image_urls4, caption="Image 4")
        except Exception as e:
            st.error(f"Error generating images: {e}")
