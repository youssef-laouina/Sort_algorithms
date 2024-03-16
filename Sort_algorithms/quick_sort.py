def quick_sort(given_list):
    n = len(given_list)

    if n <= 1:
        return given_list

    pivot = given_list[n - 1]

    small = []
    large = []
    duplicates = []

    for i in given_list:
        if i < pivot:
            small.append(i)
        elif i == pivot:
            duplicates.append(i)
        else:
            large.append(i)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + duplicates + large


my_list = [11, 2, 26, 18, 23, 23]

x = quick_sort(my_list)
print(x)