from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib


def load_sections():
    file_path = Path("rag/discharge_summary.txt")

    text = file_path.read_text(encoding="utf-8")

    sections = [
        section.strip()
        for section in text.split("\n\n")
        if section.strip()
    ]

    return sections


def build_index(sections):

    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform(sections)

    return vectorizer, vectors


if __name__ == "__main__":

    sections = load_sections()

    vectorizer, vectors = build_index(sections)

    Path("day4").mkdir(exist_ok=True)

    joblib.dump(vectorizer, "day4/tfidf_vectorizer.pkl")
    joblib.dump(vectors, "day4/document_vectors.pkl")
    joblib.dump(sections, "day4/document_sections.pkl")

    print("Discharge summaries indexed successfully.")
    print("Total sections:", len(sections))
