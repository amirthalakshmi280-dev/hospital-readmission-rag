import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv("data/sample_patients.csv")

# Input features
features = [
    "age",
    "previous_admissions",
    "length_of_stay",
    "diabetes",
    "hypertension"
]

X = data[features]
y = data["readmitted"]

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Hospital Readmission Prediction Model")
print("-------------------------------------")
print("Model Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Save trained model
joblib.dump(model, "model/readmission_model.pkl")

print("\nModel saved successfully!")
print("File: model/readmission_model.pkl")
