# Day 6 - First Working Medical RAG Assistant

## Task

Develop the first working medical RAG assistant.

## Objective

The objective is to build a simple RAG assistant that accepts patient questions and retrieves relevant information from a medical discharge summary.

## Working Process

Patient Question
        ↓
Load Discharge Summary
        ↓
Split Document into Sections
        ↓
TF-IDF Vectorization
        ↓
Similarity Calculation
        ↓
Retrieve Relevant Section
        ↓
Safe Response

## Features

- Loads discharge summaries.
- Accepts patient questions.
- Searches relevant document sections.
- Uses TF-IDF for retrieval.
- Uses cosine similarity to find relevant information.
- Provides document-based responses.
- Allows the user to exit the assistant.

## Example

Patient Question:

When is the follow-up appointment?

Assistant:

The relevant information from the discharge summary is displayed.

## Safety

The assistant uses information only from the available discharge summary.

It does not provide a new diagnosis or change treatment instructions.

If information is not available, the assistant indicates that it could not find the information.

## Files Added

- medical_rag_assistant.py
- day6_summary.md

## Status

Day 6 first working medical RAG assistant completed.

## Note

This project uses synthetic data for educational purposes and is not a medical diagnostic or clinical decision-making system.
