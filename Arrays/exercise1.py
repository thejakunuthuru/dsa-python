# Question 2 - Find pairs
# LeetCode 1 - Two Sum

def findpairs0(nums, target):
    pairs = []
    seen = set()
    
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    
    return pairs

def findpairs1(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (nums[i], nums[j])
    return None

