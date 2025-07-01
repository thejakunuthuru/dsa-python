# Question 3 - How to check if an array contains a number?

import numpy as np
my_array = np.array([1, 2, 3, 4, 5])
number_to_check = 3

def contains_number(array, number):
    for element in array:
        if element == number:
            return True
    return False                
result = contains_number(my_array, number_to_check)
print(result)  # Output: True