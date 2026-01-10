import subprocess
import sys

def execute_python_script(script_path):
    """
    Executes a Python script and streams the output in real-time.
    """
    print(f"Executing: {script_path}...")
    print("--------------------------------------------------")
    
    output_buffer = []
    
    try:
        process = subprocess.Popen(
            ["python", "-u", script_path], # -u forces unbuffered output
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )
        
        # Read stdout line by line
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                # Print to terminal immediately
                print(output.strip())
                output_buffer.append(output)
        
        # Capture any remaining stderr
        stderr_output = process.stderr.read()
        if stderr_output:
            print(f"STDERR: {stderr_output}")
            output_buffer.append(stderr_output)
            
        return_code = process.poll()
        
        full_log = "".join(output_buffer)
        
        if return_code == 0:
            print("--------------------------------------------------")
            print("Execution Successful")
            return f"SUCCESS:\n{full_log}"
        else:
            print("--------------------------------------------------")
            print("Execution Failed")
            return f"ERROR:\n{full_log}\n\nSTDERR:\n{stderr_output}"
            
    except Exception as e:
        return f"CRITICAL ERROR: {str(e)}"