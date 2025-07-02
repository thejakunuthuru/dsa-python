def pair_sum(myList, sum):
    pairs = []
    seen = set()
    
    for num in myList:
        target = sum - num
        if target in seen:
            pairs.append((target, num))
        seen.add(num)
    
    return pairs