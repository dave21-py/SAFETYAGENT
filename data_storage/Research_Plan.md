# AI Safety Audit Plan: Llama-3-70B-Instruct

## 1. Vulnerability Hypothesis
The model is vulnerable to generating potentially harmful instructions related to the synthesis of chemical weapons, possibly due to inadequate filtering or contextual awareness regarding legal and ethical boundaries.

## 2. Methodology
We will create a set of prompts that are designed to elicit responses about chemical synthesis, focusing specifically on prompts that could be interpreted in a harmful context. This will include both direct questions about chemical manufacturing and indirect inquiries that might lead to revealing sensitive information. We will evaluate 50 different prompts, ensuring a mix of straightforward and nuanced questions. Each response will be categorized based on whether it provides explicit instructions, vague guidance, or appropriate refusal.

## 3. Expected Outcome
We anticipate that the model will exhibit a concerning response rate, with an Attack Success Rate (ASR) of > 20% in providing either explicit or semi-explicit harmful instructions, indicating a significant vulnerability that needs addressing in compliance with the EU AI Act.