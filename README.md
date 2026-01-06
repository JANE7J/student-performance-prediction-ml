# 🎓 Student Performance Prediction System  
**End-to-End Machine Learning Pipeline with Flask & Interactive UI**

---

## 📌 Project Overview

This project is an **end-to-end Machine Learning pipeline** developed as part of an internship assignment.  
The system predicts a student’s **final academic performance score** based on academic factors such as study hours, attendance percentage, and previous exam scores.

The project demonstrates the **complete ML lifecycle**, starting from raw data preprocessing and model training to real-time prediction served through a **Flask REST API** and a **modern interactive web UI**.

---

## 🎯 Problem Statement

To build a machine learning system that predicts a student’s final performance score using the following inputs:

- Study hours per day  
- Attendance percentage  
- Previous exam score  

The predicted result is displayed both **numerically** and **visually** using an animated circular progress indicator.

---

## 🔄 End-to-End ML Workflow

Raw CSV Data
↓
Data Cleaning & Preprocessing
↓
Feature Selection
↓
Train–Test Split
↓
Model Training (Linear Regression)
↓
Model Evaluation (MAE, MSE, R²)
↓
Model Serialization (model.pkl)
↓
Flask REST API
↓
Interactive Web UI


---

## 🧠 Machine Learning Details

- **Algorithm Used:** Linear Regression  
- **Libraries:** Scikit-learn, Pandas, NumPy  
- **Evaluation Metrics:**
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
  - R² Score  

The trained model achieved a **high R² score (~0.99)**, indicating strong predictive performance on unseen data.

---

## 🛠️ Technology Stack

### Programming Language
- Python

### Data & ML
- Pandas
- NumPy
- Scikit-learn

### Backend
- Flask (REST API)

### Frontend
- HTML
- Tailwind CSS
- JavaScript (Fetch API)

### Tools
- Git & GitHub
- VS Code
- Postman (API testing)

---

## 📂 Project Structure

ml-pipeline-project/
│
├── data/
│ └── student.csv
│
├── src/
│ ├── preprocess.py
│ ├── train.py
│ ├── evaluate.py
│ └── predict.py
│
├── templates/
│ └── index.html
│
├── app.py
├── model.pkl
├── requirements.txt
└── README.md


---

## 🌐 Application Features

- User-friendly input form for academic details  
- Real-time prediction using trained ML model  
- Flask API for model inference  
- Animated circular progress visualization  
- Personalized output display  
- Clean and modern dark-themed UI  

---

## ▶️ How to Run the Project Locally

### Step 1: Clone the Repository
```bash
git clone https://github.com/<your-username>/student-performance-prediction-ml.git
cd student-performance-prediction-ml

Step 2: Install Dependencies

pip install -r requirements.txt

Step 3: Run the Flask Application

python app.py

Step 4: Open in Browser

http://127.0.0.1:5000

🧪 Sample Input

    Study Hours: 6

    Attendance: 80

    Previous Exam Score: 88

✅ Sample Output

    Predicted Final Score: 97%

    Output displayed using a circular progress indicator

    Personalized result shown on the UI

📌 Learning Outcomes

    Built a complete end-to-end ML pipeline

    Gained hands-on experience with model training and evaluation

    Learned model persistence using pickle

    Implemented REST APIs using Flask

    Integrated ML backend with frontend UI

    Handled real-time inference and data validation

📄 Note

The file model.pkl is a binary serialized machine learning model generated during training.
It is not meant to be opened or edited manually.
👩‍💻 Author

Neeraja
Machine Learning Intern
