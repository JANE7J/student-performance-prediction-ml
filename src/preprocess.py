import pandas as pd

def load_and_preprocess_data(file_path):
    # Load CSV
    df = pd.read_csv(file_path)

    print("Initial Data:")
    print(df.head())

    # Check missing values
    print("\nMissing values:")
    print(df.isnull().sum())

    # Drop rows with missing values (safe step)
    df = df.dropna()

    # Features and Target
    X = df[['study_hours', 'attendance', 'previous_score']]
    y = df['final_score']

    return X, y


if __name__ == "__main__":
    X, y = load_and_preprocess_data("../data/student.csv")
    print("\nFeatures (X):")
    print(X.head())

    print("\nTarget (y):")
    print(y.head())
