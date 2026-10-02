import tkinter as tk
from tkinter import messagebox
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_summary():

    file_path = Path("rag/discharge_summary.txt")

    if not file_path.exists():
        return []

    text = file_path.read_text(encoding="utf-8")

    sections = [
        section.strip()
        for section in text.split("\n\n")
        if section.strip()
    ]

    return sections


def get_answer(question, sections):

    if not sections:
        return "Discharge summary not found."

    vectorizer = TfidfVectorizer(stop_words="english")

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
        return (
            "I could not find relevant information "
            "in the discharge summary."
        )

    return (
        sections[best_index]
        + "\n\nSource: discharge_summary.txt - Section "
        + str(best_index + 1)
    )


def ask_question():

    question = question_entry.get("1.0", tk.END).strip()

    if not question:
        messagebox.showwarning(
            "Warning",
            "Please enter a question."
        )
        return

    answer = get_answer(
        question,
        sections
    )

    answer_box.config(state="normal")
    answer_box.delete("1.0", tk.END)
    answer_box.insert(tk.END, answer)
    answer_box.config(state="disabled")


def clear_text():

    question_entry.delete("1.0", tk.END)

    answer_box.config(state="normal")
    answer_box.delete("1.0", tk.END)
    answer_box.config(state="disabled")


sections = load_summary()

root = tk.Tk()
root.title("Medical RAG Assistant")
root.geometry("700x500")

title = tk.Label(
    root,
    text="Medical RAG Assistant",
    font=("Arial", 20, "bold")
)

title.pack(pady=15)

instruction = tk.Label(
    root,
    text="Ask a question about the discharge summary:",
    font=("Arial", 12)
)

instruction.pack()

question_entry = tk.Text(
    root,
    height=4,
    width=70
)

question_entry.pack(pady=10)

ask_button = tk.Button(
    root,
    text="Ask Question",
    command=ask_question
)

ask_button.pack(pady=5)

clear_button = tk.Button(
    root,
    text="Clear",
    command=clear_text
)

clear_button.pack(pady=5)

answer_label = tk.Label(
    root,
    text="Assistant Response:",
    font=("Arial", 12, "bold")
)

answer_label.pack(pady=10)

answer_box = tk.Text(
    root,
    height=12,
    width=70
)

answer_box.pack()

answer_box.config(state="disabled")

root.mainloop()
