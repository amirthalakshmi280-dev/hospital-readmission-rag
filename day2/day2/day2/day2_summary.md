# Day 2 - Project Development

## Task

Develop the readmission-risk model and define the RAG workflow using discharge summaries.

## Completed Work

### 1. Readmission Risk Model

A Random Forest Classifier was developed to predict 30-day hospital readmission risk.

### Features Used

- Age
- Previous Admissions
- Length of Stay
- Diabetes
- Hypertension

### 2. RAG Workflow

A RAG-style retrieval workflow was defined for answering patient questions from medical discharge summaries.

### RAG Steps

1. Load discharge summary
2. Split document into sections
3. Convert text using TF-IDF
4. Accept patient question
5. Calculate cosine similarity
6. Retrieve the most relevant section
7. Return the relevant answer

## Files Added

- model_results.txt
- rag_workflow.md
- day2_summary.md

## Status

Day 2 development completed successfully.

## Note

This project uses synthetic data for educational purposes and is not a medical diagnostic system.
