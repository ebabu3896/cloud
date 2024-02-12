
def find_sequence(nums):
    hashSet = set(nums)
    longest = 0
    for n in hashSet:
        length = 0
        if n - 1 not in hashSet:
            while (n + length) in hashSet:
                length += 1
        longest = max(length, longest) 
    return longest

nums = [100,4,200,1,3,2]
print(find_sequence(nums))