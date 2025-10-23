import subprocess
import os
import sys

scripts = [
    "linear_search.py",
    "binary_search.py",
    "jump_search.py",
    "interpolation_search.py",
    "exponential_search.py"
]

print("\n===== Python Search Algorithms Benchmark =====\n")

for script in scripts:
    if not os.path.exists(script):
        print(f"Error: Script not found at {script}")
        continue

    print(f"Running: {script}\n")
    subprocess.run([sys.executable, script])
