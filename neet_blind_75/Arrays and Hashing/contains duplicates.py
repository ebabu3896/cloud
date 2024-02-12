#Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

def find_dup(nums):
    find_dup = set()
    for i in nums:
        if i in find_dup:
            return True
        find_dup.add(i)
    
nums = [1,1,1,3,3,4,3,2,4,2]
print(find_dup(nums)) 