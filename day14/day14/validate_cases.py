import csv


def predict_risk(age, previous_admissions, length_of_stay):

    score = 0

    if age >= 60:
        score += 1

    if previous_admissions >= 2:
        score += 1

    if length_of_stay >= 7:
        score += 1

    if score >= 2:
        return "High"

    elif score == 1:
        return "Medium"

    return "Low"


def validate_cases():

    file_path = "day14/test_patient_cases.csv"

    total = 0
    passed = 0

    print("Patient Case Validation")
    print("-----------------------")

    with open(file_path, newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            total += 1

            age = int(row["age"])
            admissions = int(
                row["previous_admissions"]
            )
            stay = int(
                row["length_of_stay"]
            )

            expected = row["expected_risk"]

            predicted = predict_risk(
                age,
                admissions,
                stay
            )

            if predicted == expected:
                status = "PASS"
                passed += 1
            else:
                status = "FAIL"

            print(
                row["patient_id"],
                "| Expected:",
                expected,
                "| Predicted:",
                predicted,
                "|",
                status
            )

    print("\nTotal Cases:", total)
    print("Passed:", passed)
    print("Failed:", total - passed)


if __name__ == "__main__":
    validate_cases()
