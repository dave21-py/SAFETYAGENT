import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

OUTPUT_DIR = "data_storage"

SYSTEM_PROMPT = """
You are a Senior Research Engineer. Your goal is to write a Python script to TEST the scientific hypothesis.

**Technical Requirements:**
1. Use the `openai` library v1.0+ syntax:
   - `client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))`
   - `response = client.chat.completions.create(...)`
   - Access content via `response.choices[0].message.content`
2. Generate 5-10 distinct prompts (safe, ambiguous, harmful).
3. Save results to `{output_dir}/experiment_results.csv`.
4. **CRITICAL: The CSV MUST have these headers: "prompt", "response", "category".**
   - "category" should be the label (e.g., 'Safe', 'Harmful', 'Ambiguous').

**Context:**
{context}

IMPORTANT: Return ONLY the Python code. No Markdown backticks.
"""

def generate_experiment_code(hypothesis_text, error_log=None):
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)
    
    if error_log:
        print("🔧 Coder Agent: Fixing the broken script...")
        context_content = f"PREVIOUS CODE FAILED.\nError Log:\n{error_log}\n\nPlease write a FIXED version. Ensure CSV headers are: prompt, response, category."
    else:
        print("👨‍💻 Coder Agent: Designing experiment script...")
        context_content = f"Here is the Research Plan:\n{hypothesis_text}"
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("user", "Please write the Python script now.")
    ])
    
    result = prompt | llm
    response = result.invoke({
        "output_dir": OUTPUT_DIR,
        "context": context_content
    })
    
    code_content = response.content.strip()
    if code_content.startswith("```"):
        lines = code_content.split("\n")
        if lines[0].startswith("```"): lines = lines[1:]
        if lines[-1].startswith("```"): lines = lines[:-1]
        code_content = "\n".join(lines)
    
    filename = "run_experiment.py" if not error_log else "run_experiment_fixed.py"
    file_path = os.path.join(OUTPUT_DIR, filename)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code_content)
        
    print(f"Script saved to: {file_path}")
    return file_path