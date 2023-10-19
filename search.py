def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)


def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


def search(arr, k):
    original_arr = list(arr)
    quicksort(arr, 0, len(arr) - 1)
    element = arr[-k]
    position = original_arr.index(element)
    return f"елемент за індексом- {element}, позиція елементу- {position}"


arr = [15, -7, 22, 9, 36, 2, 42, 18]

k = 1

print(search(arr, k))
