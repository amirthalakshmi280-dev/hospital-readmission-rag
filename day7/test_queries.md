# Day 7 - Patient Query Testing

## Objective

Test different patient queries against the medical discharge summary.

## Test Query 1

Question:

When is the follow-up appointment?

Expected Result:

The assistant should retrieve the follow-up appointment information from the discharge summary.

## Test Query 2

Question:

What should the patient monitor?

Expected Result:

The assistant should retrieve information about monitoring from the discharge summary.

## Test Query 3

Question:

What medicines were prescribed?

Expected Result:

The assistant should retrieve the medication information available in the discharge summary.

## Test Query 4

Question:

What are the discharge instructions?

Expected Result:

The assistant should retrieve the relevant discharge instructions.

## Test Query 5

Question:

What is the patient's diet recommendation?

Expected Result:

The assistant should retrieve the diet-related information if it is available in the discharge summary.

## Test Query 6

Question:

What should I do if my symptoms become worse?

Expected Result:

The assistant should retrieve the relevant safety or follow-up information from the discharge summary.

## Testing Rule

The assistant should answer using only information available in the discharge summary.

It should not invent information when the answer is not available.
