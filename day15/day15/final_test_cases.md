# Final System Test Cases

## Test Case 1 - Readmission Risk

Input:

Age = 65
Previous Admissions = 2
Length of Stay = 7

Expected:

High Risk

Status:

PASS

---

## Test Case 2 - Patient Query

Question:

When is the follow-up appointment?

Expected:

Retrieve relevant information from the discharge summary.

Status:

PASS

---

## Test Case 3 - Monitoring Query

Question:

What should the patient monitor?

Expected:

Retrieve relevant monitoring information.

Status:

PASS

---

## Test Case 4 - Unsupported Query

Question:

What is the patient's bank account number?

Expected:

The assistant should not provide private or unavailable information.

Status:

PASS

---

## Test Case 5 - Unrelated Query

Question:

What is the weather today?

Expected:

The assistant should not use unrelated discharge-summary information as the answer.

Status:

PASS

---

## Test Case 6 - Source Citation

Question:

What are the discharge instructions?

Expected:

Display relevant information with a discharge-summary source citation.

Status:

PASS

---

## Final Validation

The complete system was checked for:

- Risk prediction
- Patient query processing
- Document retrieval
- Response relevance
- Safety controls
- Source citations
- User interface

Overall Status:

PASS
