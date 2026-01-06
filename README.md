🎓 Student Performance Prediction System

End-to-End Machine Learning Pipeline with Flask & Interactive UI

📌 Project Overview

This project is an end-to-end Machine Learning pipeline built as part of an internship assignment.
The system predicts a student’s final performance score based on academic factors such as study hours, attendance percentage, and previous exam scores.

The project demonstrates the complete ML workflow, starting from raw data and ending with a real-time prediction served through a Flask API and a modern interactive UI.

🎯 Problem Statement

Predict student performance using machine learning by analyzing:

Study hours per day

Attendance percentage

Previous exam score

The predicted output is shown both numerically and visually using a circular progress indicator.

🧠 Machine Learning Pipeline
Raw Data (CSV)
      ↓
Data Cleaning & Preprocessing
      ↓
Feature Engineering
      ↓
Train–Test Split
      ↓
Model Training (Linear Regression)
      ↓
Model Evaluation (MAE, MSE, R²)
      ↓
Model Saving (model.pkl)
      ↓
Flask REST API
      ↓
Interactive Web UI

🛠️ Technology Stack
Programming Language

Python

Data Handling

Pandas

NumPy

Machine Learning

Scikit-learn

Linear Regression model

Backend

Flask (REST API)

Frontend

HTML

Tailwind CSS

JavaScript (Fetch API)

Tools

Git & GitHub

VS Code

Postman (API testing)

📂 Project Structure
ml-pipeline-project/
│
├── data/
│   └── student.csv
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── templates/
│   └── index.html
│
├── app.py
├── model.pkl
├── requirements.txt
└── README.md

📊 Model Details

Algorithm Used: Linear Regression

Evaluation Metrics:

Mean Absolute Error (MAE)

Mean Squared Error (MSE)

R² Score

The model achieved a high R² score (~0.99) on the test dataset, indicating strong predictive performance.

🌐 Application Features

User-friendly UI to input academic details

Real-time prediction using trained ML model

Animated circular progress visualization

Personalized output (shows predicted result with user name)

Flask API integration with frontend

▶️ How to Run the Project Locally
Step 1: Clone the Repository
git clone <your-github-repo-link>
cd ml-pipeline-project

Step 2: Install Dependencies
pip install -r requirements.txt

Step 3: Run the Flask App
python app.py

Step 4: Open in Browser
http://127.0.0.1:5000

🧪 Sample Input

Study Hours: 6

Attendance: 80

Previous Score: 88

✅ Sample Output

Predicted Final Score: 97%

Displayed visually using a circular progress ring

📌 Learning Outcomes

Built a complete ML pipeline from scratch

Learned model training, evaluation, and persistence

Implemented REST APIs using Flask

Integrated ML backend with frontend UI

Handled real-time inference and data type validation

📄 Note

model.pkl is a binary file containing the trained machine learning model and is generated during training.

👩‍💻 Author

Neeraja
Intern – Machine Learning