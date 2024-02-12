# Product of Array Except Self

#Given an integer array nums, return an array answer such that answer[i] 
# is equal to the product of all the elements of nums except nums[i].

#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

#You must write an algorithm that runs in O(n) time and without using the division operation.

def find_product(nums):
    prefix = 1
    output_arr = []
    for i in range(len(nums)):
        output_arr.append(prefix)
        prefix = prefix * nums[i]
    postfix = 1
    for i in range(len(nums) -1, -1, -1):
        output_arr[i] = output_arr[i] * postfix
        postfix = postfix * nums[i]
    return output_arr
nums = [1,2,3,4]
print(find_product(nums))