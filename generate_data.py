import random
import pandas as pd

def generate_data(n=10_00_0000, filename="data.csv"):
    arr = [random.randint(1, n*10) for _ in range(n)]
    df = pd.DataFrame(arr, columns=["value"])
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    generate_data()
