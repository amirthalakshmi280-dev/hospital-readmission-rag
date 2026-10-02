from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_discharge_summary():
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


def retrieve_information(question, sections):

    if not sections:
        return "No discharge summary is available."

    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform(
        sections + [question]
    )

    similarity = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    ).flatten()

    best_index = similarity.argmax()

    return sections[best_index]


def safe_response(answer):

    if not answer:
        return (
            "I could not find this information in the "
            "available discharge summary."
        )

    return answer


def main():

    print("===================================")
    print("   MEDICAL RAG ASSISTANT")
    print("===================================")

    sections = load_discharge_summary()

    if not sections:
        print("Discharge summary not found.")
        return

    print("Discharge summary loaded successfully.")
    print("You can ask questions about the summary.")
    print("Type 'exit' to stop.")

    while True:

        question = input("\nPatient Question: ")

        if question.lower() == "exit":
            print("Assistant closed.")
            break

        answer = retrieve_information(
            question,
            sections
        )

        response = safe_response(answer)

        print("\nAssistant:")
        print(response)


if __name__ == "__main__":
    main()
