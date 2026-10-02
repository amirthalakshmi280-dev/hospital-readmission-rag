# Irrelevant Retrieval Testing

## Objective

Identify cases where the RAG system retrieves information that is not relevant to the patient's question.

## Test 1

Patient Query:

What is the patient's favorite food?

Expected:

The discharge summary may not contain this information.

Result:

The system should not return unrelated information.

Status:

REVIEW

## Test 2

Patient Query:

What is the patient's school name?

Expected:

This information is not expected to be present in a medical discharge summary.

Result:

The system should not retrieve unrelated medical information.

Status:

REVIEW

## Test 3

Patient Query:

What is the patient's bank account number?

Expected:

This information should not be available in the discharge summary.

Result:

The system should not provide private or unrelated information.

Status:

PASS

## Test 4

Patient Query:

What is the weather today?

Expected:

This is unrelated to the discharge summary.

Result:

The RAG system should not use unrelated document sections as an answer.

Status:

PASS

## Identification Rule

A retrieval is considered irrelevant when the retrieved document section does not answer or support the patient's question.

## Handling

If no relevant information is found, the system should clearly indicate that the information is not available in the discharge summary.
