import tkinter as tk
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------------
# Readmission Risk Model
# -----------------------------

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


# -----------------------------
# Load Discharge Summary
# -----------------------------

def load_summary():

    file_path = Path("rag/discharge_summary.txt")

    if not file_path.exists():
        return []

    text = file_path.read_text(
        encoding="utf-8"
    )

    sections = [
        section.strip()
        for section in text.split("\n\n")
        if section.strip()
    ]

    return sections


# -----------------------------
# RAG Retrieval
# -----------------------------

def retrieve_information(question, sections):

    if not sections:
        return None, None

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    vectors = vectorizer.fit_transform(
        sections + [question]
    )

    scores = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    ).flatten()

    best_index = scores.argmax()
    best_score = scores[best_index]

    if best_score < 0.10:
        return None, None

    source = (
        "discharge_summary.txt - Section "
        + str(best_index + 1)
    )

    return sections[best_index], source


# -----------------------------
# Ask Question
# -----------------------------

def ask_question():

    question = question_entry.get(
        "1.0",
        tk.END
    ).strip()

    if not question:
        return

    answer, source = retrieve_information(
        question,
        sections
    )

    if answer is None:

        response = (
            "I could not find relevant information "
            "in the discharge summary."
        )

    else:

        response = (
            answer
            + "\n\nSource: "
            + source
        )

    answer_box.config(state="normal")

    answer_box.delete(
        "1.0",
        tk.END
    )

    answer_box.insert(
        tk.END,
        response
    )

    answer_box.config(state="disabled")


# -----------------------------
# Calculate Risk
# -----------------------------

def calculate_risk():

    try:

        age = int(age_entry.get())
        admissions = int(
            admission_entry.get()
        )
        stay = int(
            stay_entry.get()
        )

        risk = predict_risk(
            age,
            admissions,
            stay
        )

        risk_label.config(
            text="Readmission Risk: " + risk
        )

    except ValueError:

        risk_label.config(
            text="Enter valid numbers."
        )


# -----------------------------
# GUI
# -----------------------------

sections = load_summary()

root = tk.Tk()

root.title(
    "Integrated Medical Assistant"
)

root.geometry(
    "750x650"
)


title = tk.Label(
    root,
    text="Medical RAG Assistant",
    font=("Arial", 20, "bold")
)

title.pack(pady=10)


# Patient Details

patient_label = tk.Label(
    root,
    text="Patient Information",
    font=("Arial", 14, "bold")
)

patient_label.pack()


age_entry = tk.Entry(root)

age_entry.insert(
    0,
    "65"
)

age_entry.pack(pady=5)

admission_entry = tk.Entry(root)

admission_entry.insert(
    0,
    "2"
)

admission_entry.pack(pady=5)

stay_entry = tk.Entry(root)

stay_entry.insert(
    0,
    "7"
)

stay_entry.pack(pady=5)


risk_button = tk.Button(
    root,
    text="Calculate Readmission Risk",
    command=calculate_risk
)

risk_button.pack(pady=8)


risk_label = tk.Label(
    root,
    text="Readmission Risk: Not Calculated",
    font=("Arial", 12, "bold")
)

risk_label.pack(pady=5)


# RAG Question

question_label = tk.Label(
    root,
    text="Ask a question about the discharge summary:",
    font=("Arial", 12)
)

question_label.pack(pady=10)


question_entry = tk.Text(
    root,
    height=4,
    width=70
)

question_entry.pack()


ask_button = tk.Button(
    root,
    text="Ask Question",
    command=ask_question
)

ask_button.pack(pady=8)


# Answer

answer_label = tk.Label(
    root,
    text="Assistant Response:",
    font=("Arial", 12, "bold")
)

answer_label.pack(pady=5)


answer_box = tk.Text(
    root,
    height=12,
    width=75
)

answer_box.pack()

answer_box.config(
    state="disabled"
)


root.mainloop()
