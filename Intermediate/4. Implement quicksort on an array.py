# 4.Implement quicksort on an array.

def quicksort(arr):
    if len(arr) <= 1:  # Base case: array of length 0 or 1 is already sorted
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choose the middle element as pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Example usage:
arr = [34, 7, 23, 32, 5, 62]
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)


# Output

# Sorted array: [5, 7, 23, 32, 34, 62]