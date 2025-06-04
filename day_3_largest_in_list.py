lst = input().split(" ")

def largest_in_list(lst):
    largest = float('-inf')
    for i in lst:
        if int(i) > largest:
            largest = int(i)
    return largest
print(largest_in_list(lst))