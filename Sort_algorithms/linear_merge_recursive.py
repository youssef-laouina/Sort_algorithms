def linear_merge(list1, list2, merged=None):
    if merged is None:
        merged = []

    if not list1:
        merged.extend(list2)
        return merged
    if not list2:
        merged.extend(list1)
        return merged

    if list1[0] < list2[0]:
        merged.append(list1[0])
        return linear_merge(list1[1:], list2, merged)
    else:
        merged.append(list2[0])
        return linear_merge(list1, list2[1:], merged)


print(linear_merge(['aab', 'aad', 'aaf', 'aah'], ['aac', 'aae', 'aag'], ['first element']))
