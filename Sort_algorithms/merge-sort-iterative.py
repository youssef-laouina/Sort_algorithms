def merge_sort_iterative(arr):
    n = len(arr)
    size = 1
    while size < n:
        left = 0
        while left < n - 1:
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            merge(arr, left, mid, right)
            left += 2 * size
        size *= 2


def merge(arr, left, mid, right):
    temp = [0] * (right - left + 1)
    i = left
    j = mid + 1
    k = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Copy the sorted elements back to the original array
    for m in range(len(temp)):
        arr[left + m] = temp[m]


# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort_iterative(arr)
print(arr)
