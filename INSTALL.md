# 🍒 Cherry AI — Installation Guide (Beta)

This guide explains how to install and run **Cherry AI** locally.

---

## 1️⃣ Requirements

- Windows 10 / 11  
- Python **3.11**
- NVIDIA GPU (recommended, CPU also works)
- Minimum 8 GB RAM

---

## 2️⃣ Download Cherry AI

### Download ZIP
1. Click **Code → Download ZIP**
2. Extract the folder

3️⃣ Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate

4️⃣ Install Dependencies
pip install -r requirements.txt
⚠️ This may take time. Please be patient.

5️⃣ Model Setup (Manual)
Models are NOT included in GitHub to keep the repo free and lightweight.
Create folders:
models/
 ├── llm/
 └── sd15/
Download required models as mentioned in documentation.

6️⃣ Run Cherry AI
python main.py
If everything is correct, you will see:
🍒 Cherry AI is ready

⚠️ Beta Notice
This is a Beta version.
Some features are still under development:
Voice input
Improved multi-image understanding
Online features

👤 Creator
Cherry AI is created and maintained by Vineel,
B.Tech 1st year student (AI & ML).

Built with the help of AI Models.
