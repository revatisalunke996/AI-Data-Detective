import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def train_model(df, target_column):

    # Keep only numeric columns
    numeric_df = df.select_dtypes(
        include=["number"]
    ).copy()

    # Check target column
    if target_column not in numeric_df.columns:
        return (
            None,
            "Selected target column must be numeric."
        )

    # Remove missing values
    numeric_df = numeric_df.dropna()

    # Check data size
    if len(numeric_df) < 5:
        return (
            None,
            "Not enough data to train the model."
        )

    # Target
    y = numeric_df[target_column]

    # Features
    X = numeric_df.drop(
        columns=[target_column]
    )

    # Check features
    if X.shape[1] == 0:
        return (
            None,
            "At least one feature column is required."
        )

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Create model
    model = LinearRegression()

    # Train model
    model.fit(
        X_train,
        y_train
    )

    # Predictions
    predictions = model.predict(
        X_test
    )

    # Accuracy
    accuracy = r2_score(
        y_test,
        predictions
    )

    # Actual vs predicted
    prediction_results = pd.DataFrame({
        "Actual": y_test.values,
        "Predicted": predictions
    })

    return (
        model,
        round(accuracy * 100, 2),
        prediction_results
    )