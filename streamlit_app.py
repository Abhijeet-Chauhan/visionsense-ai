import os
from dotenv import load_dotenv
import streamlit as st
import torch
from PIL import Image
import numpy as np
import pytesseract
from gtts import gTTS
import io
import time
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()

st.set_page_config(
    page_title="VisionSense AI",
    page_icon="👁️",
    layout="wide"
)

# Main title
st.markdown("<h1> 👁️‍🗨️VisionSense AI </h1>", unsafe_allow_html=True)
st.markdown("Your All in One visual companion 🧑‍🤝‍🧑", unsafe_allow_html=True)

# Custom CSS for animations and styling
st.markdown("""
    <style>
        .stTitle {
            animation: fadeIn 1.5s ease-in;
        }
        .css-1v0mbdj.etr89bj1 {
            margin-top: 2rem;
            border-radius: 10px;
            padding: 1.5rem;
            background: linear-gradient(to right, #f6f8fa, #ffffff);
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .process-step {
            animation: slideIn 0.8s ease-out;
        }
        @keyframes slideIn {
            from { transform: translateX(-20px); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        .fancy-header {
            background: linear-gradient(45deg, #2e7aff, #4c4cff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700;
            padding: 0.5rem 0;
        }
    </style>
""", unsafe_allow_html=True)

# Google Gemini setup
gemini_api_key = os.getenv("GEMINI_API_KEY")
scene_model = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=gemini_api_key)

# Load the YOLOv5 model
@st.cache_resource
def load_model():
    return torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

model = load_model()

# Function to generate a scene description using Gemini
def describe_scene(objects_info="", text_info=""):
    prompt = f"Describe the content of the image with the following information:\n"
    if objects_info:
        prompt += f"Objects detected: {objects_info}\n"
    if text_info:
        prompt += f"Text detected: {text_info}\n"
    
    try:
        response = scene_model.generate(prompts=[prompt])
        if response and response.generations:
            scene_description = response.generations[0][0].text
            return scene_description.strip()
        return "Could not generate a scene description."
    except Exception as e:
        st.error(f"Error in generating scene description: {e}")
        return f"Error generating description: {str(e)}"

# Object Detection with YOLOv5
def detect_objects(image_np):
    results = model(image_np)
    detected_objects = results.pandas().xyxy[0]
    annotated_image = np.array(results.render()[0])
    object_details = []
    for _, row in detected_objects.iterrows():
        object_details.append(f"{row['name']} (confidence: {row['confidence']:.2f})")
    return object_details, annotated_image

# Text Recognition with Tesseract OCR
def recognize_text(image):
    text = pytesseract.image_to_string(image, lang="eng")
    return text.strip()

# Text-to-Speech with gTTS
def text_to_speech(text):
    tts = gTTS(text)
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer


# Create columns for better layout
col1, col2 = st.columns([2, 1])

with col1:
    uploaded_file = st.file_uploader("📤 Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image_bytes = uploaded_file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    image_np = np.array(image)
    
    with col2:
        st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("🔍 Analyze Image", use_container_width=True):
        progress_bar = st.progress(0)
        
        # Text Recognition with animation
        st.markdown("<div class='process-step'>", unsafe_allow_html=True)
        st.markdown("### 👁️ Recognizing Text...")
        detected_text = recognize_text(image)
        progress_bar.progress(33)
        time.sleep(0.5) 
        
        if detected_text:
            st.success(f"📝 Text Found: {detected_text}")
            with st.expander("🔊 Listen to Detected Text"):
                st.audio(text_to_speech(detected_text), format="audio/mp3")
        else:
            st.info("No text detected in the image")
        st.markdown("</div>", unsafe_allow_html=True)

        # Object Detection with animation
        st.markdown("<div class='process-step'>", unsafe_allow_html=True)
        st.markdown("### 🔍 Detecting Objects...")
        objects, annotated_image = detect_objects(image_np)
        progress_bar.progress(66)
        time.sleep(0.5)
        
        st.image(annotated_image, caption="Detected Objects", use_container_width=True)
        if objects:
            st.success(f"🔍 Found Objects: {', '.join(objects)}")
        else:
            st.info("No objects detected")
        st.markdown("</div>", unsafe_allow_html=True)

        # Scene Understanding with animation
        st.markdown("<div class='process-step'>", unsafe_allow_html=True)
        st.markdown("### 🧠 Understanding Scene...")
        with st.spinner("🤔 Analyzing the scene..."):
            scene_description = describe_scene(objects_info=", ".join(objects), text_info=detected_text)
            progress_bar.progress(100)
            time.sleep(0.5)
            
            if scene_description and "Error" not in scene_description:
                st.success(f"🎉 Scene Analysis: {scene_description}")
            else:
                st.error(f"❌ Analysis Error: {scene_description}")
        st.markdown("</div>", unsafe_allow_html=True)

        # Remove progress bar after completion
        progress_bar.empty()

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "Built with ❤️‍🔥 by Abhijeet 😉 using YOLOv5, Tesseract OCR, and Gemini AI"
    "</div>",
    unsafe_allow_html=True
)