# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

def twoSum(nums, target):
    hashMap = {}
    for i, n in enumerate(nums):
        res = target - n
        if res in hashMap:
            return [i, hashMap[res]]
        else:
            hashMap[n] = i
    return []

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))