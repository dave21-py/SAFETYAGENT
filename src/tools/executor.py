import subprocess
import os
from unittest import result


def execute_python_script(script_path):
    """
    Executes a Python script and returns the stdout/stderr.
    Mimics the 'Executing command' logs seen in MatAgent.
    """
    print(f"Executing: {script_path}...")

    try:
        result = subprocess.run(
            ["python", script_path],
            capture_output=True,
            text=True,
            timeout=60 # if running after 60, stop for safety
        )

        if result.returncode == 0:
            print("✅ Execution Successful")
            return f"SUCCESS:\n{result.stdout}"
        else:
            print("❌ Execution Failed")
            return f"ERROR:\n{result.stderr}"
    except Exception as e:
        return f"CRITICAL ERROR: {str(e)}"