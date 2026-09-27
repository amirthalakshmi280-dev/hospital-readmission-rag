def create_patient_context(age, previous_admissions, length_of_stay,
                           diabetes, hypertension, risk):

    context = {
        "age": age,
        "previous_admissions": previous_admissions,
        "length_of_stay": length_of_stay,
        "diabetes": diabetes,
        "hypertension": hypertension,
        "readmission_risk": risk
    }

    return context


if __name__ == "__main__":

    patient = create_patient_context(
        age=65,
        previous_admissions=2,
        length_of_stay=7,
        diabetes=1,
        hypertension=1,
        risk="High"
    )

    print("Patient Context")
    print("----------------")

    for key, value in patient.items():
        print(key, ":", value)
