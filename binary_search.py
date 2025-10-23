import time
import psutil
import pandas as pd

df = pd.read_csv("data.csv")
arr = sorted(df["value"].tolist())
target = arr[len(arr)//2]

process = psutil.Process()

def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    start_time = time.time()
    result = binary_search(arr, target)
    end_time = time.time()
    mem_mb = process.memory_info().rss / (1024**2)

    print("================= Profiling: Binary Search =================")
    print(f"Execution Time      : {end_time - start_time:.4f} seconds")
    print(f"Peak Memory Usage   : {mem_mb:.2f} MB")
    print(f"Search Result Index : {result}")
    print("===========================================================")
