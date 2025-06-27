shoppingList = ["milk", "eggs", "bread", "butter"]

print(shoppingList[0])  # Accessing the first item
print(shoppingList[2])  # Accessing the third item
print(shoppingList[-1])  # Accessing the last item

print('milk' in shoppingList)  # Checking if 'milk' is in the list
print('cheese' in shoppingList)  # Checking if 'cheese' is in the list

for item in shoppingList:  # Iterating through the list
    print(item)

for i in range(len(shoppingList)):  # Iterating using index
    shoppingList[i] = shoppingList[i].upper()  # Converting each item to uppercase
    print(shoppingList[i])

mylist = [1, 2, 3, 4, 5]
print(mylist)
mylist[2] = 10  # Changing the third item
print(mylist)
# Time complexity for accessing an element is O(1)
# Time complexity for iterating through the list is O(n)
# Time complexity for changing an element is O(1)
# Space complexity for storing a list is O(n)
# Space complexity for iterating through a list is O(1) since we are not using any additional space that grows with the input size.
# Space complexity for changing an element is O(1) since we are modifying the list in place.

# Insertion in a list
mylist.insert(2, 20)  # Inserting 20 at index 2
print(mylist)  # Output: [1, 2, 20, 3, 4, 5]
# Time complexity for insertion is O(n) in the worst case
# Space complexity for insertion is O(1) since we are modifying the list in place.  

# Appending to a list
mylist.append(6)  # Appending 6 to the end of the list
print(mylist)  # Output: [1, 2, 20, 3, 4, 5, 6]
# Time complexity for appending is O(1) on average
# Space complexity for appending is O(1) since we are modifying the list in place.

# Extending a list
mylist.extend([7, 8, 9])  # Extending the list with new elements
print(mylist)  # Output: [1, 2, 20, 3, 4, 5, 6, 7, 8, 9]
# Time complexity for extending is O(k) where k is the number of elements being added
# Space complexity for extending is O(k) since we are adding k new elements to the list 

# Slicing a list
sliced_list = mylist[2:5]  # Slicing from index 2 to index 5
print(sliced_list)  # Output: [20, 3, 4]
# Time complexity for slicing is O(k) where k is the size of the slice
# Space complexity for slicing is O(k) since we are creating a new list with k elements 

# Updating a list with slicing
mylist[2:5] = [6, 7, 8]  # Updating the slice from index 2 to 5
print(mylist)  # Output: [1, 2, 6, 7, 8, 5, 6, 7, 8, 9]
# Time complexity for updating a slice is O(k) where k is the size of the slice
# Space complexity for updating a slice is O(1) since we are modifying the list in place

# Reversing a list
mylist.reverse()  # Reversing the list in place
print(mylist)  # Output: [9, 8, 7, 6, 5, 4, 3, 20, 2, 1]
# Time complexity for reversing is O(n)
# Space complexity for reversing is O(1) since we are modifying the list in place.

# popping an item from a list
popped_item = mylist.pop()  # Popping the last item
print(popped_item)  # Output: 1
print(mylist)  # Output: [9, 8, 7, 6, 5, 4, 3, 20, 2]
# Time complexity for popping is O(1) for the last item
# Space complexity for popping is O(1) since we are modifying the list in place.

# Popping an item from a specific index
popped_item_index = mylist.pop(3)  # Popping the item at index 3
print(popped_item_index)  # Output: 6
print(mylist)  # Output: [9, 8, 7, 5, 4, 3, 20, 2]
# Time complexity for popping from a specific index is O(n) in the worst case
# Space complexity for popping from a specific index
# is O(1) since we are modifying the list in place.

# Inserting an item at a specific index
mylist.insert(3, 5)  # Inserting 5 at index 3
print(mylist)  # Output: [9, 8, 7, 5, 5, 4, 3, 20, 2]
# Time complexity for inserting at a specific index is O(n) in the worst case
# Space complexity for inserting at a specific index is O(1) since we are modifying the list in place.  
# Lists in Python allow for dynamic resizing and are mutable, meaning we can change their contents.

# Deleting an item from a list
del mylist[3]  # Deleting the item at index 3
print(mylist)  # Output: [9, 8, 7, 5, 4, 3, 20, 2]
# Time complexity for deleting an item is O(n) in the worst case
# Space complexity for deleting an item is O(1) since we are modifying the list in place.

# Removing an item from a list
mylist.remove(20)  # Removing the first occurrence of 20
print(mylist)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Time complexity for removing an item is O(n) in the worst case
# Space complexity for removing an item is O(1) since we are modifying the list in place.

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = a + b  # Concatenating two lists
print(c)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Time complexity for concatenation is O(n + m) where n and m are the lengths of the two lists
# Space complexity for concatenation is O(n + m) since we are creating a new list with n + m elements 

a = [0]
a = a * 5  # Repeating the list 5 times
print(a)  # Output: [0, 0, 0, 0, 0]
# Time complexity for repeating a list is O(n * k) where n is the length of the list and k is the number of repetitions
# Space complexity for repeating a list is O(n * k) since we are creating a new list with n * k elements

b = [0, 1}
b = b * 5  # Repeating the list 5 times
print(b)  # Output: [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
# Time complexity for repeating a list is O(n * k) where n is the length of the list and k is the number of repetitions
# Space complexity for repeating a list is O(n * k) since we are creating a new list with n * k elements

# Builtin Functions:

a = [1, 2, 3, 4, 5]
print(len(a))  # Output: 5, returns the number of elements in the list
print(max(a))  # Output: 5, returns the maximum element in the list
print(min(a))  # Output: 1, returns the minimum element in the list
print(sum(a))  # Output: 15, returns the sum of all elements in the list
print(sorted(a))  # Output: [1, 2, 3, 4, 5], returns a new sorted list
print(a)  # Output: [1, 2, 3, 4, 5], original list remains unchanged
print(a.index(3))  # Output: 2, returns the index of the first occurrence of 3
print(a.count(2))  # Output: 1, returns the count of occurrences of 2 in the list
print(a.copy())  # Output: [1, 2, 3, 4, 5], returns a shallow copy of the list
print(a.clear())  # Output: None, clears the list in place
print(a)  # Output: [], original list is now empty  

a = 'spam'
b = list(a)  # Converting a string to a list of characters
print(b)  # Output: ['s', 'p', 'a', 'm']
c = ''.join(b)  # Joining the list of characters back into a string
print(c)  # Output: spam
# Time complexity for converting a string to a list is O(n) where n is the length of the string
# Space complexity for converting a string to a list is O(n) since we are creating a new list with n elements
# Time complexity for joining a list of characters into a string is O(n) where n is the number of characters in the list
# Space complexity for joining a list of characters into a string is O(n) since we are creating a new string with n characters  

# Sliptting a string into a list of words
sentence = "Hello, how are you?"
words = sentence.split()  # Splitting the string into a list of words
print(words)  # Output: ['Hello,', 'how', 'are', 'you?']
# Time complexity for splitting a string is O(n) where n is the length of the string
# Space complexity for splitting a string is O(k) where k is the number of words
# in the string, since we are creating a new list with k elements.

# Delimited splitting
csv_data = "name,age,city"
fields = csv_data.split(',')  # Splitting the string by comma
print(fields)  # Output: ['name', 'age', 'city']
# Time complexity for delimited splitting is O(n) where n is the length of the string
# Space complexity for delimited splitting is O(k) where k is the number of fields,
# since we are creating a new list with k elements. 

# Joining a list of strings into a single string
words = ['Hello,', 'how', 'are', 'you?']
sentence = ' '.join(words)  # Joining the list of words into a single string
print(sentence)  # Output: Hello, how are you?
# Time complexity for joining a list of strings is O(n) where n is the total length
# of all strings in the list
# Space complexity for joining a list of strings is O(n) since we are creating a new
# string with the total length of all strings in the list.

# Joining a list of strings with a specific delimiter
csv_data = ['name', 'age', 'city']
csv_string = ','.join(csv_data)  # Joining the list with a comma
print(csv_string)  # Output: name,age,city
# Time complexity for joining a list of strings with a specific delimiter is O(n) where n is the total length of all strings in the list
# Space complexity for joining a list of strings with a specific delimiter is O(n) since we are creating a new string with the total length of all strings in the list.

