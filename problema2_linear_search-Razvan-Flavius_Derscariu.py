# Problema 2 – Căutare liniară (15p)
from typing import List, Any
def linear_search(a: List[Any], x: Any) -> bool:
    for i in range(len(a)):
        if a[i] == x:
            return True
    return False

def linear_seach_output_position(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    arr = [4, 7, 1, 9]
    print(linear_search(arr, 7))  # True
    print(linear_seach_output_position(arr, 7))     # 1
    print(linear_seach_output_position(arr, 10))    # -1
