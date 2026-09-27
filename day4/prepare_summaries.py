from pathlib import Path


def load_discharge_summary(file_path):
    path = Path(file_path)

    if not path.exists():
        print("Discharge summary not found.")
        return ""

    return path.read_text(encoding="utf-8")


def prepare_summary(text):
    sections = [
        section.strip()
        for section in text.split("\n\n")
        if section.strip()
    ]

    return sections


if __name__ == "__main__":

    file_path = "rag/discharge_summary.txt"

    text = load_discharge_summary(file_path)

    sections = prepare_summary(text)

    print("Prepared Discharge Summary")
    print("--------------------------")

    for i, section in enumerate(sections, start=1):
        print(f"\nSection {i}:")
        print(section)

    print("\nTotal Sections:", len(sections))
