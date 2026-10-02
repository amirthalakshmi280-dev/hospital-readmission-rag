# Day 7 - Patient Query and Retrieval Testing

## Task

Test patient queries and discharge-summary retrieval.

## Objective

The objective is to test whether the medical RAG assistant can retrieve relevant information from discharge summaries for different patient questions.

## Testing Process

1. Load the discharge summary.
2. Enter a patient question.
3. Compare the question with document sections.
4. Retrieve the most relevant section.
5. Display the retrieved information.
6. Check whether the result is relevant.

## Queries Tested

- Follow-up appointment
- Patient monitoring
- Medication information
- Discharge instructions
- Diet recommendation
- Safety and worsening symptoms

## Result

The RAG assistant was tested with multiple patient queries.

Relevant discharge-summary information was retrieved for the tested queries.

## Status

Day 7 testing completed successfully.

## Safety

The assistant should only use information available in the discharge summary.

It should not invent medical information or provide unsupported medical advice.

## Note

This project uses synthetic data for educational purposes and is not a medical diagnostic or clinical decision-making system.
