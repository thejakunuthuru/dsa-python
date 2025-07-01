## Function to find the missing number in an array of size n containing numbers from 1 to n
# The array contains one number missing from the sequence.
# The function returns the missing number.
# The approach is to calculate the expected sum of numbers from 1 to n and subtract the
# actual sum of the numbers present in the array.
# This solution has a time complexity of O(n) and a space complexity of O(1

def missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Example usage
print(missing_number([1, 2, 3, 4, 6], 6))  # Output: 5ß