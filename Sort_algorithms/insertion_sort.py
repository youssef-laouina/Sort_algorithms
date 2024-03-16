def insertion_sort(given_list):
    n = len(given_list)

    for i in range(1, n):
        key = given_list[i]
        j = i - 1
        while key < given_list[j] and j >= 0:
            given_list[j + 1] = given_list[j]
            j -= 1
        given_list[j + 1] = key
    return given_list


print(insertion_sort([11, 2, 26, 18, 23]))

