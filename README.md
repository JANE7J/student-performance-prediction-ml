# 🎓 Student Performance Prediction System  
### End-to-End Machine Learning Pipeline with Flask & Interactive UI

---

## 📌 Project Overview

This project is an **end-to-end Machine Learning pipeline** developed as part of an internship assignment.  
The system predicts a student’s **final academic performance score** based on academic and behavioral factors.

The project demonstrates the **complete ML workflow**, starting from raw data preprocessing to real-time prediction served through a **Flask REST API** and visualized using a **modern interactive web UI**.

---

## 🎯 Problem Statement

To predict a student’s final performance score using Machine Learning based on the following features:

- Study hours per day  
- Attendance percentage  
- Previous exam score  

The output is displayed both as a **numeric score** and a **visual circular progress indicator**, making the prediction intuitive and user-friendly.

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
- **Target Variable:** Final performance score  
- **Evaluation Metrics:**
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
  - R² Score  

The trained model achieved a **high R² score (~0.99)**, indicating strong predictive performance on the test data.

---

## 🌐 Application Features

- User-friendly input form for student details  
- Real-time prediction using a trained ML model  
- Flask-based REST API for inference  
- Animated circular progress visualization of results  
- Personalized output display (shows predicted result with user name)  

---

## 🛠️ Technology Stack

### Programming Language
- Python

### Data Handling
- Pandas
- NumPy

### Machine Learning
- Scikit-learn
- Linear Regression

### Backend
- Flask (REST API)

### Frontend
- HTML
- Tailwind CSS
- JavaScript (Fetch API)

### Tools
- Git & GitHub
- VS Code
- Postman (for API testing)

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

## ▶️ How to Run the Project Locally

### Step 1: Clone the Repository
```bash
git clone https://github.com/JANE7J/student-performance-prediction-ml.git
cd student-performance-prediction-ml

Step 2: Install Dependencies

pip install -r requirements.txt

Step 3: Run the Flask Application

python app.py

Step 4: Open in Browser

http://127.0.0.1:5000

🧪 Sample Input

    Study Hours per Day: 6

    Attendance Percentage: 80

    Previous Exam Score: 88

✅ Sample Output

    Predicted Final Score: 97%

    Visualized using an animated circular progress indicator

📚 Learning Outcomes

    Built a complete end-to-end Machine Learning pipeline

    Implemented data preprocessing, model training, and evaluation

    Learned model serialization and reuse using pickle

    Deployed an ML model using Flask REST API

    Integrated backend ML inference with a frontend UI

    Implemented real-time prediction and visualization

📄 Notes

    model.pkl is a binary file containing the trained ML model.

    It is generated during the training process and used for inference.

    The file is not meant to be opened or edited manually.

👩‍💻 Author

Neeraja
Machine Learning Intern
