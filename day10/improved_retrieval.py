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


def retrieve_relevant_section(question, sections):

    if not sections:
        return None

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

    # Minimum similarity threshold
    if best_score < 0.10:
        return None

    return sections[best_index]


def safe_answer(question, sections):

    result = retrieve_relevant_section(
        question,
        sections
    )

    if result is None:
        return (
            "I could not find relevant information "
            "in the available discharge summary."
        )

    return result


if __name__ == "__main__":

    sections = load_summary()

    print("Improved Medical RAG Retrieval")
    print("------------------------------")

    question = input("Patient Question: ")

    answer = safe_answer(
        question,
        sections
    )

    print("\nAssistant:")
    print(answer)
