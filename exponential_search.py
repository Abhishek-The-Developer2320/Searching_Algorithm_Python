import time
import psutil
import pandas as pd

df = pd.read_csv("data.csv")
arr = sorted(df["value"].tolist())
target = arr[len(arr)//2]

process = psutil.Process()

def binary_search(arr, low, high, target):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    return binary_search(arr, i//2, min(i, n-1), target)

if __name__ == "__main__":
    start_time = time.time()
    result = exponential_search(arr, target)
    end_time = time.time()
    mem_mb = process.memory_info().rss / (1024**2)

    print("================= Profiling: Exponential Search =================")
    print(f"Execution Time      : {end_time - start_time:.4f} seconds")
    print(f"Peak Memory Usage   : {mem_mb:.2f} MB")
    print(f"Search Result Index : {result}")
    print("===========================================================")
