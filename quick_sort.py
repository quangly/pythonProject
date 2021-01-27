# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot

def quick_sort(sequence):
    items_greater = []
    items_lower = []
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

        for item in sequence:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)

        return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


arr = [10, 7, 8, 9, 1, 5]
print("Array: " + str(arr))
print("Quick Sorted Array: " + str(quick_sort(arr)))