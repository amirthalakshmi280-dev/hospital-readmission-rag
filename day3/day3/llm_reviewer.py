from static_analysis import analyze_code


def explain_issue(issue):
    issue_type = issue["type"]
    message = issue["message"]

    if issue_type == "Syntax Error":
        explanation = (
            "The code contains a syntax error. "
            "Check the reported line and correct the Python syntax."
        )

    elif issue_type == "Code Quality":
        explanation = (
            "This is a code-quality issue. "
            "The code may work, but it can be improved "
            "for better readability and maintainability."
        )

    else:
        explanation = (
            "The static analyzer detected an issue that "
            "should be reviewed by the developer."
        )

    return {
        "issue": message,
        "explanation": explanation
    }


def review_file(file_path):
    issues = analyze_code(file_path)

    print("LLM Reviewer")
    print("------------")

    if not issues:
        print("No issues were found.")
        return

    for issue in issues:
        result = explain_issue(issue)

        print(f"\nLine: {issue['line']}")
        print("Issue:", result["issue"])
        print("Explanation:", result["explanation"])


if __name__ == "__main__":
    review_file("predict.py")
