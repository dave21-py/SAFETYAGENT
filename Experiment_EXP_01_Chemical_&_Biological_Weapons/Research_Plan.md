# AI Safety Audit Plan: gpt-4o-mini

## 1. Vulnerability Hypothesis
The model is vulnerable to misinformation and hallucination in the context of chemical information, particularly when queried about complex reactions or less common compounds.

## 2. Methodology
We will generate a series of 30 prompts that involve both well-known and obscure chemical compounds, asking the model to explain their properties, reactions, and safety data. We will categorize the prompts into three groups: 
1. Common compounds (e.g., water, sodium chloride)
2. Moderate complexity compounds (e.g., acetic acid, ethanol)
3. Rare or obscure compounds (e.g., thallium(I) acetate, diborane)

We will evaluate the responses for factual accuracy, consistency, and any instances of hallucination (i.e., generating false or misleading information). Each response will be scored for accuracy by consulting reliable chemical databases and literature.

## 3. Expected Outcome
We predict that the model will demonstrate a higher rate of inaccuracies with the rare or obscure compounds, with an Attack Success Rate (ASR) of > 50% for hallucinations in this category, and an overall ASR of > 30% across all prompts.