class SegmentTree:
    def __init__(self, total, Lindex, Rindex):
        self.sum = total
        self.left = None
        self.right = None
        self.Lindex = Lindex
        self.Rindex = Rindex
    
    @staticmethod
    def build(nums, Lindex, Rindex):
        if Lindex == Rindex:
            return SegmentTree(nums[Lindex], Lindex, Rindex)
        
        M = (Lindex + Rindex) // 2
        root = SegmentTree(0, Lindex, Rindex)
        root.left = SegmentTree.build(nums, Lindex, M)
        root.right = SegmentTree.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root
    
    def update(self, index, val):
        #O(logn)
        if self.Lindex == self.Rindex:
            self.sum = val
            return
        
        M = (self.Lindex + self.Rindex) // 2
        if index > M:
            self.right.update(index, val)
        else:
            self.left.update(index, val)
        self.sum = self.left.sum + self.right.sum
    
    def rangeQuery(self, Lindex, Rindex):
        if Lindex == self.Lindex and Rindex == self.Rindex:
            return self.sum
        
        M = (self.Lindex and self.Rindex) // 2
        if Lindex > M:
            return self.right.rangeQuery(Lindex, Rindex)
        elif Rindex <= M:
            return self.left.rangeQuery(Lindex, Rindex)
        else:
            return (self.left.rangeQuery(L, M) +
                    self.right.rangeQuery(M + 1, R))
        