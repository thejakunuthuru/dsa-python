lst = input().split(" ")

def second_largest_in_list(lst):
    if len(lst) < 2:
        return "List must contain at least two distinct numbers"
    else:
        largest = float('-inf')
        second_largest = float('-inf')
        
        for i in lst:
            num = int(i)
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num
                
        return second_largest if second_largest != float('-inf') else "No second largest number"
print(second_largest_in_list(lst))