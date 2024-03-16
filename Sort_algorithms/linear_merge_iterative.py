def linear_merge(list1, list2):
    n1, n2 = len(list1), len(list2)
    i1, i2 = 0, 0
    merged = []

    while i1 < n1 and i2 < n2:
        if list1[i1] < list2[i2]:
            merged.append(list1[i1])
            i1 += 1
        else:
            merged.append(list2[i2])
            i2 += 1

    while i1 < n1:
        merged.append(list1[i1])
        i1 += 1

    while i2 < n2:
        merged.append(list2[i2])
        i2 += 1

    return merged


print(linear_merge(['aab', 'aad', 'aaf', 'aah'], ['aac', 'aae', 'aag']))
