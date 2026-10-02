# Day 11 - Source Citations and Safe Responses

## Task

Add source citations and safe-response controls.

## Objective

The objective is to make RAG responses more transparent by showing the source of retrieved information and applying safety controls.

## Source Citation

The assistant identifies the discharge-summary file and section used to answer the patient query.

Example:

Source: discharge_summary.txt - Section 1

## Safe Response Controls

The assistant:

- Uses retrieved information only.
- Does not invent information.
- Reports when information is unavailable.
- Does not create unsupported diagnoses.
- Does not change medication instructions.
- Protects patient privacy.

## Workflow

Patient Question
        ↓
Document Retrieval
        ↓
Similarity Check
        ↓
Relevant Section
        ↓
Safe Response
        ↓
Source Citation

## Files Added

- cited_rag_assistant.py
- response_safety.md
- day11_summary.md

## Status

Day 11 completed successfully.

## Note

This project uses synthetic data for educational purposes and is not a medical diagnostic or clinical decision-making system.
