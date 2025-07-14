# image-classifier-api
A Django-based REST API for image classification using a CNN model

# 🧠 MNIST Digit Classifier API

A machine learning web API that classifies handwritten digits (0–9) using a Convolutional Neural Network (CNN) trained on the MNIST dataset.

---

## 🔍 Features

- 🧠 CNN model with 99%+ accuracy
- 🎯 REST API built using Django Rest Framework
- 📤 Accepts handwritten digit images via POST request
- 📥 Returns predicted digit as JSON
- 🧪 Tested with Postman

---

## 🚀 Tech Stack

- Python
- TensorFlow / Keras (CNN model)
- Django Rest Framework (API)
- NumPy, OpenCV, Pillow
- Postman (for testing)

---

## 📦 How to Run Locally

 **Clone the repo**
```bash
git clone https://github.com/Shahnazaqsa/image-classifier-api.git
cd image-classifier-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

🧪 How to Test 
- Open Postman
- Create a POST request to:
- http://127.0.0.1:8000/api/predict/
-  Under Body 
  - form-data:
  - Add a key image
  - Type: File
  - Upload any digit image (28x28 or larger)
  - Hit Send – You’ll get a response:

.
├── api/
│   ├── views.py
│   ├── utils.py
│   └── urls.py
├── classifier_api/
│   └── urls.py
├── model/
│   └── mnist_cnn_model.h5
├── manage.py
└── README.md

## Author
Shahnaz Aqsa
Machine Learning & Backend Developer


