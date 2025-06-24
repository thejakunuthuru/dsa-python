# Day 1 - 11, 15, 10, 6
# Day 2 - 2, 3, 4, 5
# Day 3 - 8, 9, 10, 11
# Day 4 - 12, 13, 14, 15

import numpy as np

two_d_array = np.array([[11, 15, 10, 6],
                        [2, 3, 4, 5],
                        [8, 9, 10, 11],
                        [12, 13, 14, 15]]) 
# O(m*n) time complexity for creating a 2D array
# O(m*n) space complexity for storing a 2D array

print(two_d_array)

# new_two_d_array = np.insert(two_d_array, 0, [16, 17, 18, 19], axis=1)  # Insert a new column at index 0
# print(new_two_d_array)

# new_two_d_array_row = np.append(new_two_d_array, [20, 21, 22, 23, 24], axis=0)  # append a new row
# print(new_two_d_array_row)

new_two_d_array_delete = np.delete(two_d_array, 0, axis=1)  # Delete the first column
print(new_two_d_array_delete)