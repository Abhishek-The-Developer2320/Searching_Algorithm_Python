import time
import psutil
import pandas as pd

# Load array from CSV
df = pd.read_csv("data.csv")
arr = df["value"].tolist()
target = arr[len(arr)//2] # You can choose any target from array

process = psutil.Process()

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

if __name__ == "__main__":
    start_time = time.time()
    result = linear_search(arr, target)
    end_time = time.time()
    mem_mb = process.memory_info().rss / (1024**2)

    print("================= Profiling: Linear Search =================")
    print(f"Execution Time      : {end_time - start_time:.4f} seconds")
    print(f"Peak Memory Usage   : {mem_mb:.2f} MB")
    print(f"Search Result Index : {result}")
    print("===========================================================")
