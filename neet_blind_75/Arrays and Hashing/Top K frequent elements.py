# Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

def find_freq(nums, k):
    hashMap = {}
    for i, n in enumerate(nums):
        if n in hashMap:
            hashMap[n] += 1
        else:
            hashMap[n] = 1
    sortedele = sorted(hashMap, key = hashMap.get, reverse=True)

    return sortedele[:k]


nums = [1,1,1,2,2,3]
k = 2
print(find_freq(nums, k))