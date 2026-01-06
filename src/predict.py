import pickle
import numpy as np

def predict_marks(study_hours, attendance, previous_score):
    # Load trained model
    with open("../model.pkl", "rb") as file:
        model = pickle.load(file)

    # Prepare input for model
    input_data = np.array([[study_hours, attendance, previous_score]])

    # Predict
    prediction = model.predict(input_data)

    return prediction[0]


if __name__ == "__main__":
    # Sample test
    result = predict_marks(6, 85, 70)
    print("Predicted Final Score:", result)
