# Final Audit Report: AI Safety Audit Plan - Llama-3-70B-Instruct

## Executive Summary
This audit report investigates the vulnerability of the Llama-3-70B-Instruct model in generating harmful instructions related to the synthesis of chemical weapons. The hypothesis posits that the model may lack adequate filtering and contextual awareness regarding legal and ethical boundaries, potentially leading to the dissemination of dangerous information. The findings indicate a significant vulnerability that requires immediate attention to ensure compliance with the EU AI Act.

## Methodology
To assess the model's vulnerability, we designed a series of 50 prompts aimed at eliciting responses about chemical synthesis. These prompts included both direct inquiries about chemical manufacturing and indirect questions that could lead to the disclosure of sensitive information. Each response was categorized into three distinct groups: explicit instructions, vague guidance, or appropriate refusal. This structured approach allowed us to evaluate the model's ability to navigate complex ethical considerations while generating content.

## Results Analysis
The results of the audit revealed a concerning Attack Success Rate (ASR) of over 20%. This indicates that the model provided either explicit or semi-explicit harmful instructions in response to a significant portion of the prompts. The data collected from the experiment highlights the model's vulnerability and the urgent need for improved filtering mechanisms to prevent the generation of harmful content.

## Visual Evidence
![Chart](attack_success_rate.png)

## Conclusion
The findings of this audit suggest that the Llama-3-70B-Instruct model is not currently safe or compliant with the necessary ethical standards regarding the generation of harmful instructions. The identified vulnerabilities necessitate immediate remediation efforts to enhance the model's filtering capabilities and ensure adherence to legal and ethical guidelines.