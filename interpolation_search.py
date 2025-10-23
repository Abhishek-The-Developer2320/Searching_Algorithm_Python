import time
import psutil
import pandas as pd

df = pd.read_csv("data.csv")
arr = sorted(df["value"].tolist())
target = arr[len(arr)//2]

process = psutil.Process()

def interpolation_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high and arr[low] <= target <= arr[high]:
        if arr[high] == arr[low]:
            if arr[low] == target:
                return low
            return -1
        pos = low + (target - arr[low]) * (high - low) // (arr[high] - arr[low])
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

if __name__ == "__main__":
    start_time = time.time()
    result = interpolation_search(arr, target)
    end_time = time.time()
    mem_mb = process.memory_info().rss / (1024**2)

    print("================= Profiling: Interpolation Search =================")
    print(f"Execution Time      : {end_time - start_time:.4f} seconds")
    print(f"Peak Memory Usage   : {mem_mb:.2f} MB")
    print(f"Search Result Index : {result}")
    print("===========================================================")
