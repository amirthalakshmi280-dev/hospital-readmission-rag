from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from patient_context import create_patient_context


def load_discharge_summary():
    file_path = Path("rag/discharge_summary.txt")

    text = file_path.read_text(encoding="utf-8")

    chunks = [
        chunk.strip()
        for chunk in text.split("\n\n")
        if chunk.strip()
    ]

    return chunks


def retrieve_answer(question, chunks):
    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform(
        chunks + [question]
    )

    similarity = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    ).flatten()

    best_index = similarity.argmax()

    return chunks[best_index]


def main():

    patient = create_patient_context(
        age=65,
        previous_admissions=2,
        length_of_stay=7,
        diabetes=1,
        hypertension=1,
        risk="High"
    )

    print("Patient Readmission Risk")
    print("------------------------")
    print("Risk:", patient["readmission_risk"])

    chunks = load_discharge_summary()

    question = input("\nAsk a question about the patient: ")

    answer = retrieve_answer(question, chunks)

    print("\nRAG Answer:")
    print(answer)


if __name__ == "__main__":
    main()
