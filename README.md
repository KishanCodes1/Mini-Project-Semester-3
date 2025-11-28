# 🔢 Handwritten Digit Recognition App

A full-stack Machine Learning application that recognizes handwritten digits (0-9) from user-uploaded images. This project uses a **Logistic Regression** model trained on the MNIST dataset and serves predictions via a **Streamlit** web interface.

## 🚀 Project Overview
This project bridges the gap between Data Science and Web Development. It takes a raw image, preprocesses it to match the MNIST dataset format (grayscale, inverted colors, 28x28 resolution), and feeds it into a trained Machine Learning model for prediction.

### Key Features
- **User-Friendly Interface:** Built with Streamlit for easy image uploading and interaction.
- **Real-Time Prediction:** Instantly classifies digits upon upload.
- **Image Preprocessing:** Automatically handles color inversion (converting black-on-white text to white-on-black) and resizing.
- **Model Accuracy:** Achieves ~92% accuracy on the test dataset.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Frontend:** Streamlit
- **Machine Learning:** Scikit-Learn (Logistic Regression)
- **Data Manipulation:** NumPy, Pandas
- **Image Processing:** PIL (Python Imaging Library)

## 📂 Project Structure
- `app.py`: The main web application script.
- `train.py`: The script used to train the model and save it.
- `digit_model.pkl`: The serialized (saved) Machine Learning model.
- `requirements.txt`: List of dependencies required to run the app.

## 💻 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME

2. Install Dependencies

Bash

pip install -r requirements.txt



3. Run the App

Bash

streamlit run app.py


4. Usage

The web app will open in your browser.

Upload an image of a handwritten digit (JPG, PNG, or JPEG).

Click "Predict Digit" to see the result.



This is the final touch that makes your project look professional. A good README.md file tells your teacher exactly what you built and how to run it.

Since you are a CS student, I have written this in Markdown format.

How to use this:
Create a new file in your VS Code folder named README.md (make sure it ends in .md).

Copy and paste the code block below into that file.

Save it, commit it, and push it to GitHub.

Copy this Code Block:
Markdown

# 🔢 Handwritten Digit Recognition App

A full-stack Machine Learning application that recognizes handwritten digits (0-9) from user-uploaded images. This project uses a **Logistic Regression** model trained on the MNIST dataset and serves predictions via a **Streamlit** web interface.

## 🚀 Project Overview
This project bridges the gap between Data Science and Web Development. It takes a raw image, preprocesses it to match the MNIST dataset format (grayscale, inverted colors, 28x28 resolution), and feeds it into a trained Machine Learning model for prediction.

### Key Features
- **User-Friendly Interface:** Built with Streamlit for easy image uploading and interaction.
- **Real-Time Prediction:** Instantly classifies digits upon upload.
- **Image Preprocessing:** Automatically handles color inversion (converting black-on-white text to white-on-black) and resizing.
- **Model Accuracy:** Achieves ~92% accuracy on the test dataset.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Frontend:** Streamlit
- **Machine Learning:** Scikit-Learn (Logistic Regression)
- **Data Manipulation:** NumPy, Pandas
- **Image Processing:** PIL (Python Imaging Library)

## 📂 Project Structure
- `app.py`: The main web application script.
- `train.py`: The script used to train the model and save it.
- `digit_model.pkl`: The serialized (saved) Machine Learning model.
- `requirements.txt`: List of dependencies required to run the app.

## 💻 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME
Install Dependencies

Bash

pip install -r requirements.txt
Run the App

Bash

streamlit run app.py
Usage

The web app will open in your browser.

Upload an image of a handwritten digit (JPG, PNG, or HEIC).

Click "Predict Digit" to see the result.
