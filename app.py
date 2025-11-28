import streamlit as st
import joblib
import numpy as np
from PIL import Image, ImageOps

# 1. Load the trained model
try:
    model = joblib.load('digit_model.pkl')
except:
    st.error("Error: 'digit_model.pkl' not found. Make sure it is in the same folder!")
    st.stop()

# 2. App Title and Description
st.title("🔢 Handwritten Digit Recognizer")
st.write("Upload a photo of a handwritten digit (0-9), and the AI will guess what it is.")

# 3. File Uploader
file = st.file_uploader("Upload an image...", type=["jpg", "png", "jpeg"])

if file is not None:
    # Open the image
    image = Image.open(file).convert("L") # Convert to Grayscale (B&W)
    
    # DISPLAY the user's original image
    st.image(image, caption="Your Image", width=200)

    # --- PRE-PROCESSING ---
    # Invert colors: MNIST is White-on-Black. Real paper is Black-on-White.
    image = ImageOps.invert(image)
    
    # Resize to 28x28 pixels (Standard MNIST size)
    image = image.resize((28, 28))
    
    # Convert image to numbers (numpy array)
    img_array = np.array(image)
    
    # Flatten the matrix (28x28 becomes 1x784)
    img_array = img_array.reshape(1, -1)

    # --- PREDICTION ---
    if st.button("Predict Digit"):
        prediction = model.predict(img_array)
        
        # Show the result
        st.success(f"I think this is the number: {prediction[0]}")
        st.balloons()