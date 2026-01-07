# AI Safety Audit Plan: Llama-3-70B-Instruct

## 1. Vulnerability Hypothesis
The model is vulnerable to the inadvertent disclosure of Personally Identifiable Information (PII) through unsafe conversational prompts.

## 2. Methodology
We will create a series of 30 conversational prompts that simulate user queries asking for sensitive information or leading the model towards generating PII-related content. These prompts will vary in context and complexity, including straightforward requests for personal data, scenarios involving identification confirmation, and social engineering tactics that could coax the model into revealing sensitive information. Each interaction will be recorded, and the responses will be analyzed to identify any instances of PII disclosure.

## 3. Expected Outcome
We anticipate that the model will inadvertently disclose PII in at least 25% of the interactions, indicating a significant risk for users engaging with the model in contexts where sensitive information is involved.