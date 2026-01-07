import os
import shutil
from dotenv import load_dotenv

load_dotenv()

from src.agents.hypothesis_agent import generate_hypothesis
from src.agents.coder_agent import generate_experiment_code
from src.agents.visualization_agent import generate_visualization_code
from src.agents.report_agent import generate_final_report
from src.agents.judge_agent import evaluate_results
from src.tools.executor import execute_python_script

# Context keywords matched to CSV Categories
EXPERIMENTS = [
    {"id": "EXP_01", "topic": "Chemical & Biological Weapons", "context": "Chemical"},
    {"id": "EXP_02", "topic": "Cybersecurity Exploits", "context": "Cybersecurity"},
    {"id": "EXP_03", "topic": "Self-Harm & Violence", "context": "Self-Harm"},
    {"id": "EXP_04", "topic": "Disinformation Campaigns", "context": "Disinformation"},
    {"id": "EXP_05", "topic": "PII Leakage", "context": "PII"},
    {"id": "EXP_06", "topic": "Copyright Infringement", "context": "Copyright"}
]

RESULTS_FILE = "data_storage/experiment_results.csv"

def run_single_experiment(exp_id, topic, context):
    print(f"\n\n==================================================")
    print(f"🚀 STARTING {exp_id}: {topic}")
    print(f"==================================================\n")
    
    if os.path.exists(RESULTS_FILE):
        os.remove(RESULTS_FILE)
    
    target_model = "Llama-3-70B-Instruct"
    
    hypothesis_doc = generate_hypothesis(target_model, context)
    script_path = generate_experiment_code(hypothesis_doc)
    
    max_retries = 3
    attempt = 0
    success = False
    
    while attempt < max_retries:
        print(f"--- 🏃 Attempt {attempt + 1} ---")
        result = execute_python_script(script_path)
        
        # CRITICAL: Print logs so we can see what happened
        print(">> SCRIPT OUTPUT START")
        print(result[-1000:]) # Print last 1000 chars of log
        print(">> SCRIPT OUTPUT END")

        if os.path.exists(RESULTS_FILE) and os.path.getsize(RESULTS_FILE) > 0:
            print("✅ Data generation successful.")
            success = True
            break
        else:
            print("❌ Data file missing or empty.")
            script_path = generate_experiment_code(hypothesis_doc, error_log=result)
            attempt += 1
            
    if success:
        try:
            print("⚖️ Running Analysis Pipeline...")
            evaluate_results("experiment_results.csv")
            
            viz_script = generate_visualization_code("experiment_results.csv")
            execute_python_script(viz_script)
            
            generate_final_report(hypothesis_doc)
            
            archive_dir = f"Experiment_{exp_id}_{topic.replace(' ', '_')}"
            os.makedirs(archive_dir, exist_ok=True)
            
            for file in ["experiment_results.csv", "attack_success_rate.png", "Final_Audit_Report.md", "Research_Plan.md"]:
                src = f"data_storage/{file}"
                if os.path.exists(src):
                    shutil.copy(src, f"{archive_dir}/{file}")
            
            print(f"🏆 Results archived to {archive_dir}")
        except Exception as e:
            print(f"❌ Analysis Failed: {e}")
    else:
        print(f"❌ {exp_id} FAILED. Review logs above.")

if __name__ == "__main__":
    for exp in EXPERIMENTS:
        run_single_experiment(exp['id'], exp['topic'], exp['context'])