def bubble_sort(arr):
    n = len(arr)
    
    # Repeat the process n times
    for i in range(n):
        # Compare adjacent elements
        for j in range(0, n - 1):
            # If the current element is greater than the next, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


# --- Test ---
my_list = [5, 2, 8, 1, 9]

print("Unsorted:", my_list)
bubble_sort(my_list)
print("Sorted:  ", my_list)

