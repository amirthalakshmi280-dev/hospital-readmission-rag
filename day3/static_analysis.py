import ast


def analyze_code(file_path):
    issues = []

    with open(file_path, "r", encoding="utf-8") as file:
        code = file.read()

    try:
        tree = ast.parse(code)
    except SyntaxError as error:
        issues.append({
            "type": "Syntax Error",
            "line": error.lineno,
            "message": str(error)
        })
        return issues

    for node in ast.walk(tree):

        # Detect print statements
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == "print":
                issues.append({
                    "type": "Code Quality",
                    "line": node.lineno,
                    "message": "Print statement found. Consider using logging in production."
                })

        # Detect unused pass statements
        if isinstance(node, ast.Pass):
            issues.append({
                "type": "Code Quality",
                "line": node.lineno,
                "message": "Empty pass statement found."
            })

    return issues


if __name__ == "__main__":
    results = analyze_code("predict.py")

    print("Static Analysis Results")
    print("-----------------------")

    if not results:
        print("No issues found.")

    for issue in results:
        print(
            f"[{issue['type']}] "
            f"Line {issue['line']}: "
            f"{issue['message']}"
        )
