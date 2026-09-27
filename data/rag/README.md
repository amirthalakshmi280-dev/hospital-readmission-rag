# Hospital Readmission Risk Prediction and RAG Bot

## Problem Statement

Predict 30-day hospital readmission risks using clinical tabular features, and construct a RAG bot to answer patient queries from medical discharge summaries.

## Project Overview

This project contains two main modules:

1. **30-Day Hospital Readmission Prediction**
2. **Medical Discharge Summary RAG Bot**

---

## 1. Hospital Readmission Prediction

A Machine Learning model is used to predict whether a patient has a risk of being readmitted to the hospital within 30 days.

### Features Used

* Age
* Previous Admissions
* Length of Stay
* Diabetes
* Hypertension

### Machine Learning Algorithm

**Random Forest Classifier**

The model is trained using sample clinical data and predicts:

* LOW Risk
* HIGH Risk

---

## 2. RAG Bot

The RAG-style chatbot answers patient questions using information from a medical discharge summary.

The bot uses:

* TF-IDF Vectorization
* Cosine Similarity
* Relevant text retrieval

### Example Questions

* When is the follow-up appointment?
* What should the patient monitor?
* What condition was the patient treated for?
* What should the patient do about medication?

---

## Project Structure

```text
hospital-readmission-rag/
│
├── data/
│   └── sample_patients.csv
│
├── model/
│
├── rag/
│   └── discharge_summary.txt
│
├── train_model.py
├── predict.py
├── rag_bot.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Requirements

Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

---

## How to Run

### Step 1: Train the Machine Learning Model

```bash
python train_model.py
```

This trains the Random Forest model and saves the trained model as:

```text
model/readmission_model.pkl
```

### Step 2: Predict Readmission Risk

```bash
python predict.py
```

Enter the patient's clinical information when prompted.

### Step 3: Run the RAG Bot

```bash
python rag_bot.py
```

Then enter questions related to the discharge summary.

---

## Example

### Input

```text
Age: 65
Previous Admissions: 2
Length of Stay: 7
Diabetes: 1
Hypertension: 1
```

### Output

```text
Readmission Risk: HIGH
```

### RAG Bot Example

```text
Patient: When is the follow-up appointment?

Bot: The patient should attend a follow-up appointment after 2 weeks.
```

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Random Forest
* TF-IDF
* Cosine Similarity
* Joblib

---

## Dataset

This project uses **synthetic/sample clinical data** for educational purposes.

No real patient information is included.

---

## Disclaimer

This project is an educational demonstration and is **not a medical diagnostic or clinical decision-making system**. Predictions should not be used for real patient care.
