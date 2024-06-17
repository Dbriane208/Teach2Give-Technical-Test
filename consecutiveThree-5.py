"""
Design a function that takes a list of integers as input. The function should
return True if the list contains two consecutive threes (3 next to a 3) anywhere
within the list. Otherwise, it should return False. For example, the function
should return True for [1, 3, 3] and False for [1, 3, 1, 3].
"""

def consecutiveThrees(nums):
    for num in range(len(nums)-1):
        if nums[num] == 3 and nums[num + 1] == 3:
            return True

    return False
        
print(consecutiveThrees([1, 3, 1, 3]))       