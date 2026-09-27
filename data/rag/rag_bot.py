import joblib

# Load trained model
model = joblib.load("model/readmission_model.pkl")

print("30-Day Hospital Readmission Risk Prediction")
print("--------------------------------------------")

# Get patient details
age = float(input("Enter Age: "))
previous_admissions = float(input("Enter Previous Admissions: "))
length_of_stay = float(input("Enter Length of Stay (days): "))
diabetes = int(input("Diabetes? (1 = Yes, 0 = No): "))
hypertension = int(input("Hypertension? (1 = Yes, 0 = No): "))

# Prepare patient data
patient = [[
    age,
    previous_admissions,
    length_of_stay,
    diabetes,
    hypertension
]]

# Predict
prediction = model.predict(patient)[0]
probability = model.predict_proba(patient)[0][1]

# Display result
if prediction == 1:
    print("\nReadmission Risk: HIGH")
else:
    print("\nReadmission Risk: LOW")

print("Estimated Risk:", round(probability * 100, 2), "%")

print("\nNote: This is an educational project using synthetic data.")
