# Safety Controls

## Objective

Improve the safety of the medical RAG assistant by preventing unsupported responses and irrelevant information.

## 1. Document-Based Answers

The assistant should answer using information available in the discharge summary.

## 2. Retrieval Threshold

A minimum similarity threshold is used during retrieval.

If the similarity score is too low, the assistant should not return an unrelated document section.

## 3. Missing Information

If relevant information is not available, the assistant should say:

"I could not find relevant information in the available discharge summary."

## 4. No Unsupported Diagnosis

The assistant should not create a diagnosis that is not present in the document.

## 5. Medication Safety

The assistant should not recommend starting, stopping, or changing medication instructions.

## 6. Patient Privacy

Do not expose real patient names, medical IDs, passwords, or other private information.

## 7. Prompt Safety

Prompts should instruct the assistant to:

- Use retrieved information only.
- Avoid guessing.
- Avoid unsupported medical advice.
- Clearly state when information is unavailable.
- Use simple and clear language.

## 8. Human Support

For medical concerns that require professional evaluation, the patient should be directed to their healthcare team or appropriate medical care.

## Summary

These controls help reduce irrelevant retrievals and unsupported responses.
