def merge(left, right):
    result = []

    while len(left) >= 1 and len(right) >= 1:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    while len(left) >= 1:
        result.append(left[0])
        left = left[1:]

    while len(right) >= 1:
        result.append(right[0])
        right = right[1:]

    return result


def merge_sort(given_list):
    n = len(given_list)

    if n == 1:
        return given_list

    left = []
    right = []

    for i in range(n):
        if i < n / 2:
            left.append(given_list[i])
        else:
            right.append(given_list[i])

    left = merge_sort(left)
    #     print(left, sep="----")

    right = merge_sort(right)
    #     print(right, sep="----")

    return merge(left, right)


merge_sort([1, 2, 36, 10, 14, 36, 12, 100, 12])
