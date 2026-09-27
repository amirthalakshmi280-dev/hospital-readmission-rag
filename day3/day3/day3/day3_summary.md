# Day 3 - Static Analysis and LLM Reviewer

## Task

Connect static-analysis results to the LLM reviewer for issue explanation.

## Objective

The objective is to analyze Python source code, identify issues, and provide simple explanations for the detected issues.

## Workflow

Python Source Code
        ↓
Static Analysis
        ↓
Detect Issues
        ↓
Issue Details
        ↓
LLM Reviewer
        ↓
Issue Explanation

## Static Analysis

The static analyzer checks the Python code and identifies basic code-quality and syntax issues.

The analyzer records:

- Issue type
- Line number
- Issue message

## LLM Reviewer

The reviewer receives the static-analysis results and converts the technical issue into a simple explanation.

## Example

Static Analysis Result:

[Code Quality] Line 10:
Print statement found.

Reviewer Explanation:

This is a code-quality issue.
The code may work, but it can be improved for better readability and maintainability.

## Files Added

- static_analysis.py
- llm_reviewer.py
- day3_summary.md

## Status

Day 3 development completed.

## Note

This implementation is an educational demonstration of connecting static-analysis output to an automated reviewer. It does not use real patient data.
