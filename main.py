import streamlit as st
import numpy as np
from PIL import Image
import cv2
from color_extraction import detect_color

def main():
    st.title("Color Detector")
    st.write("Upload an image to detect the most dominant color.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
        st.write("")
        st.write("Detecting colors...")

        image = np.array(image)
        
        most_frequent_color = detect_color(image)

        st.write(f"The most dominant color is: RGB {most_frequent_color}")

if __name__ == "__main__":
    main()
