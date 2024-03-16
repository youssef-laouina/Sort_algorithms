def bubble_sort(given_list):
    n = len(given_list)

    for i in range(n):
        for j in range(n - 1 - i):
            if given_list[j + 1] < given_list[j]:
                given_list[j + 1], given_list[j] = given_list[j], given_list[j + 1]

    return given_list


x = bubble_sort([1, 22, 2, 5, 5, 6, 5, 48, 5, 1, 56, 8, 9, 455, 6])
print(x)