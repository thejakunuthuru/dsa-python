def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 != list2:
        return False
    else:
        return True

def is_permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    count = {}
    for item in list1:
        count[item] = count.get(item, 0) + 1
    for item in list2:
        if item not in count or count[item] == 0:
            return False
        count[item] -= 1
    return True 