from array import *

# 1. Create an array and traverse it

my_array = array('i', [1, 2, 3, 4, 5])
for i in my_array: # O(n) time complexity
    print(i)

# 2. Access individual elements through indexes
print("Step 2")
print(my_array[0])  # Access first element
print(my_array[3])  # Access fourth element 

# 3. Append new elements
print("Step 3")
my_array.append(6)
print(my_array)

# 4. Insert value in an array using insert() method
print("Step 4")
my_array.insert(4, 7)  # Insert 7 at index 4
print(my_array)

# 5. Extend an array using extend() method
print("Step 5")
my_array1 = array('i', [8, 9, 10])
my_array.extend(my_array1)  # Extend with multiple elements
print(my_array)

# 6. Add items from list using fromlist() method
print("Step 6")
temp_list = [11, 12, 13]
my_array.fromlist(temp_list)  # Add items from list
print(my_array)

# 7. Remove any array element using remove() method
print("Step 7")
my_array.remove(7)  # Remove first occurrence of 7
print(my_array)

# 8. Remove last array element using pop() method
print("Step 8")
my_array.pop()  # Remove last element
print(my_array)

#9. Fetch any element through its index using index() method
print("Step 9")
index_of_11 = my_array.index(11)  # Get index of element 11
print(f"Index of 11: {index_of_11}")

# 10. Reverse a Python array using reverse() method
print("Step 10")
my_array.reverse()  # Reverse the array
print(my_array)

# 11. Get array buffer information using buffer_info() method
print("Step 11")
buffer_info = my_array.buffer_info()  # Get buffer info
print(f"Buffer info: {buffer_info}")

# 12. Check for number of occurrences of an element using count() method
print("Step 12")
count_of_11 = my_array.count(11)  # Count occurrences of 11
print(f"Count of 11: {count_of_11}")

# 13. Convert array to bytes using tobytes() method
print("Step 13")
byte_array = my_array.tobytes()  # Convert to bytes
print(f"Byte array: {byte_array}") 

# 14. Convert array to a python list using tolist() method
print("Step 14")
python_list = my_array.tolist()  # Convert to list
print(f"Python list: {python_list}")

# 15. Append a string from an array using fromstring() method
print("Step 15")
# Note: fromstring() is not applicable for integer arrays, so we will skip this step    

# 16. Slice elements from an array using slicing
print("Step 16")
sliced_array = my_array[1:4]  # Slice from index 1 to 3
print(f"Sliced array: {sliced_array}")