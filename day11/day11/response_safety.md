# Safe Response Controls

## Objective

Ensure that responses are based on retrieved discharge-summary information and include a source citation.

## 1. Source-Based Response

The assistant should answer using only information retrieved from the discharge summary.

## 2. Source Citation

Every retrieved response should identify its source.

Example:

Source: discharge_summary.txt - Section 2

## 3. Missing Information

If relevant information cannot be found, the assistant should respond:

"I could not find relevant information in the available discharge summary."

## 4. No Unsupported Information

The assistant should not add information that is not supported by the retrieved document.

## 5. Medical Safety

The assistant should not:

- Create a new diagnosis.
- Change medication instructions.
- Recommend stopping medication.
- Provide unsupported treatment advice.

## 6. Privacy

Do not expose real patient names, medical IDs, passwords, or other private information.

## 7. Human Support

For medical concerns that require professional evaluation, the user should be directed to their healthcare team or appropriate medical care.

## Summary

Source citations improve transparency, while safe-response controls reduce unsupported and potentially unsafe responses.
