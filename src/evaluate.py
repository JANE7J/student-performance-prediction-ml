import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from preprocess import load_and_preprocess_data


def evaluate_model():
    # Load data
    X, y = load_and_preprocess_data("../data/student.csv")

    # Train-Test Split (same as training)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Load trained model
    with open("../model.pkl", "rb") as file:
        model = pickle.load(file)

    # Predictions
    y_pred = model.predict(X_test)

    # Evaluation metrics
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Model Evaluation Results:")
    print("MAE :", mae)
    print("MSE :", mse)
    print("R2 Score :", r2)


if __name__ == "__main__":
    evaluate_model()
