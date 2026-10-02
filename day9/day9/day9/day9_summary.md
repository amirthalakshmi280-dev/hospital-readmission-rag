# Day 9 - Irrelevant Retrieval and Unsupported Response Detection

## Task

Identify irrelevant retrievals and unsupported responses.

## Objective

The objective is to identify cases where the RAG system retrieves unrelated information or produces responses that are not supported by the discharge summary.

## Irrelevant Retrieval

An irrelevant retrieval occurs when the retrieved document section does not answer or support the patient's question.

## Unsupported Response

An unsupported response occurs when the assistant provides information that is not available in the retrieved discharge summary.

## Detection Process

Patient Query
        ↓
Document Retrieval
        ↓
Check Relevance
        ↓
Check Supporting Evidence
        ↓
Accept or Reject Response

## Safety Checks

- Verify retrieved information.
- Do not invent information.
- Do not create diagnoses.
- Do not modify medication instructions.
- Do not provide unsupported medical advice.
- Clearly state when information is unavailable.

## Result

Several irrelevant and unsupported-response cases were identified and documented.

The system should reject unsupported information and provide only document-based responses.

## Status

Day 9 completed successfully.

## Note

This project uses synthetic data for educational purposes and is not a medical diagnostic or clinical decision-making system.
