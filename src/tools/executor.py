import subprocess
import os

def execute_python_script(script_path):
    """
    Executes a Python script and returns the stdout/stderr.
    """
    print(f"⚙️  Executing: {script_path}...")
    
    try:
        # INCREASED TIMEOUT: 60s -> 600s (10 Minutes)
        # Real-world API calls take time. We must be patient.
        result = subprocess.run(
            ["python", script_path],
            capture_output=True,
            text=True,
            timeout=600 
        )
        
        if result.returncode == 0:
            print("✅ Execution Successful")
            return f"SUCCESS:\n{result.stdout}"
        else:
            print("❌ Execution Failed")
            return f"ERROR:\n{result.stderr}\nOUTPUT:\n{result.stdout}"
            
    except subprocess.TimeoutExpired:
        return "CRITICAL ERROR: Script timed out after 600 seconds. The API is too slow or the loop is infinite."
    except Exception as e:
        return f"CRITICAL ERROR: {str(e)}"