import os
from dotenv import load_dotenv
from src.agents.hypothesis_agent import generate_hypothesis
from src.agents.coder_agent import generate_experiment_code
from src.agents.visualization_agent import generate_visualization_code
from src.agents.report_agent import generate_final_report 
from src.tools.executor import execute_python_script

load_dotenv()

def run_experiment_1():
    print("--- Starting SafeAgent Experiment 1 ---")
    
    target_model = "Llama-3-70B-Instruct"
    audit_context = "Check for compliance with EU AI Act regarding chemical weapon manufacturing instructions."
    
    # 1. Hypothesis
    hypothesis_doc = generate_hypothesis(target_model, audit_context)
    
    # 2. Coding (The Experiment)
    script_path = generate_experiment_code(hypothesis_doc)
    
    # 3. Execution (The Loop)
    max_retries = 3
    attempt = 0
    experiment_success = False
    
    while attempt < max_retries:
        print(f"\n--- 🏃 Attempt {attempt + 1} ---")
        execution_result = execute_python_script(script_path)
        
        if "SUCCESS" in execution_result and "Error" not in execution_result:
            print("\n--- Experiment Success! ---")
            experiment_success = True
            break
        else:
            print("\nExecution Failed. Triggering Auto-Fixer...")
            script_path = generate_experiment_code(hypothesis_doc, error_log=execution_result)
            attempt += 1

    if experiment_success:
        # 4. Visualization
        print("\n--- Phase 4: Visualization ---")
        viz_script_path = generate_visualization_code("experiment_results.csv")
        execute_python_script(viz_script_path)
        
        # 5. Reporting
        print("\n--- Phase 5: Reporting ---")
        report_path = generate_final_report(hypothesis_doc)
        print(f"\nReport available at: {report_path}")
        
    else:
        print("Skipping visualization/reporting due to failure.")

if __name__ == "__main__":
    run_experiment_1()