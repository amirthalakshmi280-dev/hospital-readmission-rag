# Day 14 - Test Patient Case Validation

## Task

Validate with test patient cases.

## Objective

The objective is to validate the readmission-risk component using multiple synthetic patient cases.

## Test Cases

The validation dataset contains:

- Low-risk cases
- Medium-risk cases
- High-risk cases

## Validation Process

Test Patient Data
        ↓
Readmission Risk Model
        ↓
Predicted Risk
        ↓
Compare with Expected Risk
        ↓
PASS / FAIL

## Test Features

Each test case contains:

- Patient ID
- Age
- Previous Admissions
- Length of Stay
- Expected Risk

## Result

The test cases are used to verify whether the risk model produces the expected risk category for each synthetic patient.

## Safety

All test cases use synthetic data.

No real patient information is included.

## Status

Day 14 validation completed successfully.

## Note

The risk calculation is a simple educational model and is not a clinically validated prediction system.
