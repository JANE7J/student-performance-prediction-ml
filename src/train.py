import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from preprocess import load_and_preprocess_data


def train_model():
    # Load data
    X, y = load_and_preprocess_data("../data/student.csv")

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Save Model
    with open("../model.pkl", "wb") as file:
        pickle.dump(model, file)

    print("Model trained and saved as model.pkl")


if __name__ == "__main__":
    train_model()
