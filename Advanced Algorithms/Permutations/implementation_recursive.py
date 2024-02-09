def permRecur(nums):
    return helper(0, nums)

def helper(i, nums):
    if i == len(nums):
        return [[]]
    
    resPerm = []

    perms = helper(i+1, nums)
    for p in perms:
        for j in range(len(p) + 1):
            pCopy = p.copy()
            pCopy.insert(j, nums[i])
            resPerm.append(pCopy)
    return resPerm