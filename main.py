import streamlit as st
import numpy as np
from PIL import Image
import cv2
from color_extraction import detect_colors

def main():
    st.title("Color Detector")
    st.write("Upload an image to detect the five most dominant colors.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
        st.write("")
        st.write("Detecting colors...")

        # Convert the image to an OpenCV format
        image = np.array(image)
        
        dominant_colors = detect_colors(image, num_colors=5)

        st.write("The most dominant colors are:")
        for i, (color, name) in enumerate(dominant_colors):
            st.write(f"{i+1}. RGB {color} - {name}")
            st.markdown(f'<div style="width:50px;height:50px;background-color:rgb({color[0]},{color[1]},{color[2]});"></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
