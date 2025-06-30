# 🔐 Face ID Protected Calculator

A simple GUI calculator app with **Face Recognition authentication**, built using Python and PySide6.

## 🚀 Features

- ✅ Face ID login using InsightFace
- ➕ Basic operations: `+`, `-`, `*`, `/`
- 🧮 Math functions: `sin`, `cos`, `tan`, `cot`, `log`, `factorial`
- 🖼️ Qt-based UI (`main.ui`)
- 🔒 Access granted only if your face is recognized

## 🛠 Requirements

```bash
pip install opencv-python numpy sympy insightface PySide6
```

## ▶️ How to Run
```
python main.py
```
Press q to capture your face. If it matches the saved embeddings, the calculator will launch.

## 📁 File Structure

```text
project/
├── main.ui         # Qt Designer UI file
├── face_id.npy     # Registered face embeddings
├── script.py       # Main Python script
└── README.md       # This file
```
