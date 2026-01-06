from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Convert inputs to float
    study_hours = float(data["study_hours"])
    attendance = float(data["attendance"])
    previous_score = float(data["previous_score"])

    # Create DataFrame with correct feature names
    input_df = pd.DataFrame(
        [[study_hours, attendance, previous_score]],
        columns=["study_hours", "attendance", "previous_score"]
    )

    prediction = model.predict(input_df)[0]

    percentage = round(float(prediction), 2)

    return jsonify({
        "predicted_marks": percentage,
        "percentage": int(round(percentage)),
        "student_name": "Neeraja"   # 👈 FUN + PROOF
    })


if __name__ == "__main__":
    app.run(debug=True)
