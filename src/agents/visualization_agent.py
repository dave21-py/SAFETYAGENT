import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

OUTPUT_DIR = "data_storage"

SYSTEM_PROMPT = """
You are a Data Visualization Expert.
Goal: Visualize the Attack Success Rate (ASR) comparing different models.

**Data:**
The CSV at `{csv_path}` has columns: `model`, `category`, `is_jailbroken`.

**Instructions:**
1. Read the CSV.
2. Group by `model` AND `category` to calculate ASR (mean of `is_jailbroken` * 100).
   - If only one category exists in the file, just Group by `model`.
3. Create a Bar Chart using `seaborn`.
   - X-axis: Model
   - Y-axis: ASR (%)
   - Title: "Safety Audit: ASR by Model"
   - Use a distinct color palette.
4. Save as `{output_dir}/attack_success_rate.png`.

IMPORTANT: Return ONLY the Python code.
"""

def generate_visualization_code(csv_filename="experiment_results.csv"):
    print("📊 Visualization Agent: Generating comparative plot...")
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)
    csv_path = os.path.join(OUTPUT_DIR, csv_filename)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("user", "Generate the script.")
    ])
    
    result = prompt | llm
    response = result.invoke({"output_dir": OUTPUT_DIR, "csv_path": csv_path})
    
    code = response.content.strip()
    if code.startswith("```"):
        lines = code.split("\n")
        if lines[0].startswith("```"): lines = lines[1:]
        if lines[-1].startswith("```"): lines = lines[:-1]
        code = "\n".join(lines)
        
    filename = "visualize_results.py"
    file_path = os.path.join(OUTPUT_DIR, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)
        
    print(f"✅ Viz Script saved to: {file_path}")
    return file_path