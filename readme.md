# 👁️ VisionSense AI

Hey there! Welcome to VisionSense AI - your smart companion for understanding whats in images! This app is like having a super helpful friend who can see and explain everything in pictures to you.

## 📋 Table of Contents
- [Features](#-features)
- [Requirements](#-requirements)
- [Complete Setup Guide](#-complete-setup-guide)
- [Usage Guide](#-usage-guide)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

## 🌟 Features

VisionSense AI does three cool things:
1. Reads any text in your images (yep, like magic! 🪄)
2. Spots objects and tells you what they are
3. Gives you a nice description of the whole scene

Its perfect for:
- Helping visually impaired people understand images better
- Getting text from images when you cant copy-paste
- Finding out whats in a picture when your not sure
- Just having fun seeing what AI can spot in your photos!

## 💻 Requirements

Before you start, make sure you got:
- Python 3.8 or newer
- About 2GB free disk space (for models)
- Internet connection (for first setup)
- A computer that isnt from the stone age

## 🔧 Complete Setup Guide

### 1. Python Installation
```bash
# For Windows:
1. Download Python from python.org
2. Run installer (IMPORTANT: Check "Add Python to PATH"!)
3. Open cmd and type: python --version

# For Mac:
1. Install homebrew first:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
2. brew install python

# For Linux:
sudo apt-get update
sudo apt-get install python3.8
```

### 2. Get the Project
```bash
# Clone or download the project
git clone https://github.com/abhijeet-chauhan/visionsense-ai
cd visionsense-ai
```

### 3. Setup Virtual Environment (recommended!)
```bash
# Create virtual environment
python -m venv venv

# Activate it:
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 4. Install Required Packages
```bash
# Install main requirements
pip install streamlit torch torchvision torchaudio
pip install Pillow numpy pytesseract gtts
pip install langchain-google-genai

# Install YOLOv5 requirements
pip install -r https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt
```

### 5. Install Tesseract OCR

#### Windows:
1. Download installer from: https://github.com/UB-Mannheim/tesseract/wiki
2. Run installer
3. Add to PATH: `C:\Program Files\Tesseract-OCR`

#### Mac:
```bash
brew install tesseract
```

#### Linux:
```bash
sudo apt-get install tesseract-ocr
```

### 6. Get API Keys
1. Enable Gemini API
2. Create API key
3. Save it somewhere safe!

### 7. Setup Environment Variables
Create a file named `.env`:
```
GOOGLE_API_KEY=your_api_key_here
```

### 8. Final Project Structure
Your folder should look like:
```
visionsense-ai/
├── app.py
├── .env
├── venv/
├── README.md
└── requirements.txt
```

## 🚀 How to Run

1. Make sure your virtual environment is activated
2. Run the app:
```bash
streamlit run streamlit_app.py
```
3. Should open in your browser at http://localhost:8501

## 👀 Usage Guide

### Basic Usage:
1. Click "Upload Image" button
2. Pick any image file
3. Hit "Analyze Image"
4. Wait for magic to happen!

### Advanced Features:
- Click 'Listen' button to hear text read aloud
- Hover over detected objects for confidence scores
- Use fullscreen mode for better view

## ⚠️ Troubleshooting

Common Issues & Fixes:

### "ModuleNotFoundError":
```bash
pip install -r requirements.txt
```

### "Tesseract not found":
```bash
# Windows: Check PATH
# Mac: brew install tesseract
# Linux: sudo apt-get install tesseract-ocr
```

### "CUDA error":
```python
# In app.py, add:
device = 'cpu'  # Force CPU usage
```

### "Memory Error":
- Try smaller images
- Close other applications
- Restart your computer

## 🤝 Contributing

I love help! Here's how:
1. Fork the repo
2. Create new branch
3. Make changes
4. Create pull request
5. Wait for virtual high-five!

## 🛠️ Tech Stack I Used

- YOLOv5 - the thing that spots objects (its super fast!)
- Tesseract OCR - for reading text in images
- Gemini AI - the smart brain that describes everything
- Streamlit - makes everything look nice and pretty
- Python - holds everything together!

## 📝 License

Feel free to use this however you want! Just be cool about it and maybe give me a shoutout if you make something awesome with it.

Made with ❤️‍🔥 and probably too much coffee ☕

---
PS: If something breaks, try turning it off and on again. Works 90% of the time, every time! 😉

Need more help? Create an issue or [email me](mailto:abhijeetchauhan025@example.com)!
