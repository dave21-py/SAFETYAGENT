import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

OUTPUT_DIR = "data_storage"

SYSTEM_PROMPT = """
You are a Data Visualization Expert for a Scientific Paper.
Your goal is to write a Python script that visualizes the results of an AI Safety Experiment.

**Data Structure:**
The CSV at `{csv_path}` contains raw experiment data with columns: `prompt`, `response`, `category`.

**Instructions:**
1. Read the CSV file.
2. **Calculate the value counts** for the 'category' column (Safe, Ambiguous, Harmful).
   - Example: `counts = data['category'].value_counts().reset_index()`
   - Rename columns to 'Category' and 'Count'.
3. Create a professional Bar Chart using `seaborn`.
   - X-axis: 'Category'
   - Y-axis: 'Count'
4. Add a title: "Attack Success Rate by Category".
5. Save the figure as `{output_dir}/attack_success_rate.png`.
6. Use `plt.tight_layout()` to ensure nothing is clipped.

IMPORTANT: Return ONLY the Python code. No Markdown.
"""

def generate_visualization_code(csv_filename="experiment_results.csv"):
    print("📊 Visualization Agent: Generating plot script...")
    
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)
    
    csv_path = os.path.join(OUTPUT_DIR, csv_filename)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("user", "Generate the visualization script now.")
    ])
    
    result = prompt | llm
    response = result.invoke({
        "output_dir": OUTPUT_DIR,
        "csv_path": csv_path
    })
    
    code_content = response.content.strip()
    if code_content.startswith("```"):
        lines = code_content.split("\n")
        if lines[0].startswith("```"): lines = lines[1:]
        if lines[-1].startswith("```"): lines = lines[:-1]
        code_content = "\n".join(lines)
        
    filename = "visualize_results.py"
    file_path = os.path.join(OUTPUT_DIR, filename)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code_content)
        
    print(f"Viz Script saved to: {file_path}")
    return file_path