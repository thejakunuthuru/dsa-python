# def remove_duplicates(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if i != j and arr[i] == arr[j]:
#                 arr.pop(j)
#     return arr

def remove_duplicates(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]

print(remove_duplicates(arr))   