# Max Product of Two Integers in an Array
# This function finds the maximum product of two integers in an array.

def max_product(arr):
    if len(arr) < 2:
        return None  # Not enough elements to form a product

    max1 = max(arr)
    arr.remove(max1)
    max2 = max(arr)

    return max1 * max2

def max_product_alternative(arr):
    if len(arr) < 2:
        return None  # Not enough elements to form a product

    max1 = float('-inf')
    max2 = float('-inf')

    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

    return max1 * max2

def max_product_alternative2(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if i == j:
                continue
            elif arr[i] * arr[j] > max_product:
                max_product = arr[i] * arr[j]
    return max_product
