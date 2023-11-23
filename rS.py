import random

def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_select(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_index = partition(arr, low, high)

    if k == pivot_index:
        return arr[pivot_index]
    elif k < pivot_index:
        return randomized_select(arr, low, pivot_index - 1, k)
    else:
        return randomized_select(arr, pivot_index + 1, high, k)

def find_median(arr):
    n = len(arr)
    if n % 2 == 0:
        # Wenn die Anzahl der Elemente gerade ist, finden wir den Index des rechten Medians
        median_index = n // 2
    else:
        # Wenn die Anzahl der Elemente ungerade ist, finden wir den Index des Medians
        median_index = (n - 1) // 2

    return randomized_select(arr, 0, len(arr) - 1, median_index)

# Beispiel
arr = [3, 1, 4, 44, 122, 2, 5, 35]
sort=arr.sort()
median = find_median(arr)
print(f"Median: {median}")
