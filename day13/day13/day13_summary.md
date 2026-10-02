# Day 13 - Risk Model, RAG and UI Integration

## Task

Integrate risk model, RAG and UI.

## Objective

The objective is to combine the readmission-risk prediction, RAG retrieval system and graphical user interface into one medical assistant application.

## Integrated Components

### 1. Risk Model

The system uses patient information such as:

- Age
- Previous admissions
- Length of stay

These values are used to calculate a sample readmission-risk category.

### 2. RAG System

The RAG component:

- Loads the discharge summary.
- Processes document sections.
- Retrieves relevant information.
- Shows the source section.

### 3. User Interface

The GUI provides:

- Patient information input
- Risk calculation button
- Readmission-risk display
- Patient question input
- RAG answer display
- Source citation

## Workflow

Patient Information
        ↓
Readmission Risk Model
        ↓
Risk Result

Patient Question
        ↓
RAG Retrieval
        ↓
Relevant Discharge Information
        ↓
Safe Response

Both components are integrated through the graphical interface.

## Safety

The application uses synthetic data for demonstration.

It does not provide a medical diagnosis or replace professional medical advice.

## Files Added

- integrated_medical_assistant.py
- day13_summary.md

## Status

Day 13 completed successfully.
