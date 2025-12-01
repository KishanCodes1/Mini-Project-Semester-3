
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
    image = Image.open(file).convert("L") # Convert to Grayscale
    
    # Show original
    st.image(image, caption="Original Image", width=150)

    # --- BETTER PRE-PROCESSING ---
    
    # 1. Invert colors (If needed)
    # Check if image is mostly light (white paper). If so, invert to make it black background.
    if np.mean(np.array(image)) > 127:
        image = ImageOps.invert(image)

    # 2. Smart Thresholding (Contrast Boost) BEFORE Resizing
    # Doing this on the high-res image keeps the digit thick.
    img_array_temp = np.array(image)
    # Any pixel less than 50 becomes 0, anything else becomes 255
    img_array_temp = np.where(img_array_temp > 50, 255, 0).astype(np.uint8)
    image = Image.fromarray(img_array_temp)

    # 3. Resize to 28x28 (Standard MNIST) using LANCZOS for quality
    image = image.resize((28, 28), Image.Resampling.LANCZOS)
    
    # 4. Convert to float array for the model
    img_array = np.array(image, dtype=np.float32)

    # Show what the AI sees (Debugging)
    # Note: We must cast to uint8 to display with Streamlit/PIL correctly
    st.image(image, caption="What the AI sees", width=150)
    
    # 5. Normalize (0-1) and Flatten
    img_array = img_array / 255.0  
    img_array = img_array.reshape(1, -1)

    # --- PREDICTION ---
    if st.button("Predict Digit"):
        prediction = model.predict(img_array)
        probs = model.predict_proba(img_array)
        confidence = np.max(probs) * 100
        
        st.success(f"🎯 Prediction: **{prediction[0]}**")
        st.write(f"Confidence: **{confidence:.2f}%**")

        st.balloons() # Fun visual effect

        # Optional: Show breakdown
        # st.bar_chart(probs[0])