def first_second(my_list):
    my_list_sorted = sorted(my_list)
    return my_list_sorted[ : -3 : -1]

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(first_second(myList)) # 90 87

def first_second2(my_list):
    max1, max2 = float('-inf'), float('-inf')
 
    for num in my_list:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
 
    return max1, max2
 
my_list2 = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second2(my_list2))  # Output: (90, 87)