lst = input().split(" ")

def smallest_in_list(lst):
    smallest = float('inf')
    for i in lst:
        if int(i) < smallest:
            smallest = int(i)
    return smallest
print(smallest_in_list(lst))