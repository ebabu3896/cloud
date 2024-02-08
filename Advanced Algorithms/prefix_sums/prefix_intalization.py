class PrefixSum:
    def __init__(self,nums):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)
    
    def find_sum(self):
        print(self.prefix)
        print(nums)

    def rangeSum(self, left, right):
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 0 else 0
        return (preRight - preLeft)


nums = [2, -1, 3, -3, 4]
pre = PrefixSum(nums)
pre.find_sum()
print(pre.rangeSum(1, 4))