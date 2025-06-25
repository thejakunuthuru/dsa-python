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