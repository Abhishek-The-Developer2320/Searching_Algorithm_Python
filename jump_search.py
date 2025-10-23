import time
import psutil
import math
import pandas as pd

df = pd.read_csv("data.csv")
arr = sorted(df["value"].tolist())
target = arr[len(arr)//2]

process = psutil.Process()

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    start_time = time.time()
    result = jump_search(arr, target)
    end_time = time.time()
    mem_mb = process.memory_info().rss / (1024**2)

    print("================= Profiling: Jump Search =================")
    print(f"Execution Time      : {end_time - start_time:.4f} seconds")
    print(f"Peak Memory Usage   : {mem_mb:.2f} MB")
    print(f"Search Result Index : {result}")
    print("===========================================================")
