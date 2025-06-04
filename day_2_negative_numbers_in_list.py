lst = input().split(" ")
def negative_numbers_in_list(lst):
    count = 0
    for i in lst:
        if int(i) < 0:
            count += 1
    return count
print(negative_numbers_in_list(lst))