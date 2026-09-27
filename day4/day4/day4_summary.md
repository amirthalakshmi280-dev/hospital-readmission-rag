# Day 4 - Discharge Summary Preparation and Indexing

## Task

Prepare and index discharge summaries for retrieval.

## Objective

The objective is to prepare medical discharge summaries into smaller sections and create a searchable index for the RAG pipeline.

## Step 1: Load Discharge Summary

The discharge summary is loaded from:

rag/discharge_summary.txt

## Step 2: Prepare the Summary

The document is divided into smaller sections using paragraph separation.

Each section is stored separately for retrieval.

## Step 3: Create TF-IDF Index

TF-IDF is used to convert the discharge summary sections into numerical vectors.

These vectors are used to compare patient questions with the stored document sections.

## Step 4: Store the Index

The following files are generated:

- tfidf_vectorizer.pkl
- document_vectors.pkl
- document_sections.pkl

## Workflow

Discharge Summary
        ↓
Load Document
        ↓
Split into Sections
        ↓
TF-IDF Vectorization
        ↓
Create Document Index
        ↓
Store Index
        ↓
Ready for Retrieval

## Files Added

- prepare_summaries.py
- build_index.py
- day4_summary.md

## Status

Day 4 completed successfully.

## Note

This project uses synthetic data for educational purposes. It is not a medical diagnostic or clinical decision-making system.
