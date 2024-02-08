# Given an array of intergers, return indices of the two numbers such that they add up to a specific target
#you may assume that each input would have exactly one solution and you may not use same element twiice.
#eg: [2,1,5,3], Target = 4

# To solve this problem in better we need to understand hash map algorithm. 

#Bruteforce method (conceputal)

# def find_val(List1, n):
#     for i in range(1, len(List1)):
#         for j in range(i):
#             if List1[j] + List1[i] == 4:
#                 return True
#     return False

#Time Complexity = O(N^2)
#I am getting false, as result, where is the mistake?
# The issue in your code is in the line if List1[j] + List1[j+1] == 4:. 
# Instead of checking the sum of the elements at indices j and j+1, you should be checking the sum of the elements at indices j and i to see if it equals the target value.


#2. Using Hash Map [Better Method]
# List1 = [2,1,5,3]
# n = 4

# class Solution:
#     def twoSum(self, nums, target):
#         prevMap = {}  # using Hash map by creating a dict and adding the data into it.
#         for i,n in enumerate(nums):  # i is index and n is value
#             diff = target-n
#             if diff in prevMap:
#                 return [prevMap[diff], i]
#             prevMap[n] = i
#         return


# find = Solution()
# print(find.twoSum(List1,n))

#Time Complexity is O(n log n)


#3. Optimal approach without using Hashmap using 2 pointer approach/Greedy approch.
List1 = [2,1,5,3]
n = 4
class Solution:
    def twoSum(self, nums,target):
        nums.sort()
        left = 0
        right = len(nums)-1
        while(left < right):
            sum = nums[left] + nums[right]
            if(sum == target):
                return "YES"
            elif sum < target:
                left += 1
            else:
                right -= 1
        return "NO"

find = Solution()
find.twoSum(List1, n)

#Time Complexity O(N) + O(nlog N)[sorting]
#space Complextiy O(1)
#Observed one error:
#The issue in your code is in the lines where you are updating the left and right pointers inside the while loop. 
#You should be incrementing left when the current sum is less than the target, and decrementing right when the sum is greater than the target.