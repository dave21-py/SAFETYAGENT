import os
import openai
import pandas as pd

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the function to test the scientific hypothesis
def test_hypothesis(hypothesis):
    try:
        # Simulate using 'gpt-4o-mini' if testing a non-OpenAI model
        model = "gpt-4o-mini" if hypothesis.startswith("Llama-3") else "gpt-4"

        # Create a chat completion request
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "user", "content": hypothesis}
            ]
        )

        # Extract the response content
        result = response.choices[0].message.content
        return result

    except Exception as e:
        return str(e)

# Hypothesis to test
hypothesis = "Does Llama-3 outperform traditional models in natural language processing?"

# Run the test
result = test_hypothesis(hypothesis)

# Save results to CSV
results_df = pd.DataFrame({"Hypothesis": [hypothesis], "Result": [result]})
results_df.to_csv('data_storage/experiment_results.csv', index=False)