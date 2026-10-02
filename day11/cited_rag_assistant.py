from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_document():
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


def retrieve_with_source(question, sections):

    if not sections:
        return None, None

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
        return None, None

    source = f"discharge_summary.txt - Section {best_index + 1}"

    return sections[best_index], source


def safe_response(answer, source):

    if answer is None:
        return (
            "I could not find relevant information "
            "in the available discharge summary."
        )

    response = (
        "Based on the available discharge summary:\n\n"
        + answer
        + "\n\nSource: "
        + source
    )

    return response


def main():

    print("================================")
    print("   CITED MEDICAL RAG ASSISTANT")
    print("================================")

    sections = load_document()

    if not sections:
        print("Discharge summary not found.")
        return

    question = input("\nPatient Question: ")

    answer, source = retrieve_with_source(
        question,
        sections
    )

    response = safe_response(
        answer,
        source
    )

    print("\nAssistant:")
    print(response)


if __name__ == "__main__":
    main()
