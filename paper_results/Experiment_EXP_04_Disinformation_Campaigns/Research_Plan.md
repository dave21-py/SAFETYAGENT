# AI Safety Audit Plan: Llama-3-70B-Instruct

## 1. Vulnerability Hypothesis
The model is vulnerable to generating and propagating disinformation, particularly in contexts where it mimics authoritative sources or presents information as factual.

## 2. Methodology
We will conduct a series of tests where we prompt the model with questions that are likely to elicit responses containing disinformation. This will include:
- Creating 30 prompts that reflect current events, scientific claims, and controversial topics, each designed to elicit potentially misleading or false information.
- Varying the phrasing of the prompts to assess how the model's responses change based on specificity and context (e.g., using authoritative language or casual language).
- Implementing a control set of prompts that reference well-documented facts to compare the accuracy of the responses.
- Evaluating the model's responses using a team of experts to rate the factual accuracy and identify instances of disinformation.

## 3. Expected Outcome
The expectation is that at least 25% of the responses will contain disinformation, as indicated by expert review. This would suggest a significant vulnerability in the model's handling of factual information, particularly in nuanced contexts.