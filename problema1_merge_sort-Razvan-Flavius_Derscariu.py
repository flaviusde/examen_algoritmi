# Problema 1 – Merge Sort (20p)
# TODO: Implementați algoritmul Merge Sort și explicați complexitatea.
# Complexitate: O(n log n)

from typing import List

def merge_sort(a: List[int]) -> List[int]:
    if len(a) > 1:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
    return a

if __name__ == "__main__":
    data = [5, 2, 8, 1, 3]
    print("input :", data)
    print("sorted:", merge_sort(data))
