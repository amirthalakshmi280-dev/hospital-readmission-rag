# RAG Workflow

## Objective

To answer patient questions using information from medical discharge summaries.

## Workflow

Discharge Summary
        ↓
Load Document
        ↓
Split into Sections
        ↓
TF-IDF Vectorization
        ↓
Patient Question
        ↓
Cosine Similarity
        ↓
Retrieve Relevant Section
        ↓
Return Answer

## Step 1: Load Document

The discharge summary is stored in:

rag/discharge_summary.txt

## Step 2: Text Processing

The discharge summary is divided into smaller sections.

## Step 3: Vectorization

TF-IDF is used to convert the document sections into numerical vectors.

## Step 4: Patient Query

The patient enters a question.

Example:

When is the follow-up appointment?

## Step 5: Similarity Calculation

Cosine similarity compares the patient question with each document section.

## Step 6: Information Retrieval

The section with the highest similarity is selected.

## Step 7: Answer

The relevant information is returned to the patient.

## Example

Question:

What should the patient monitor?

Answer:

The patient should monitor blood glucose regularly.
Blood pressure should also be monitored as advised by the healthcare team.

## Technologies

- Python
- Scikit-learn
- TF-IDF
- Cosine Similarity

## Safety

This project uses synthetic data and is intended only for educational purposes. It is not a medical diagnostic or clinical decision-making system.
