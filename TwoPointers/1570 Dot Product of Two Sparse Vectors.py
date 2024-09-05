class SparseVector:
    def __init__(self, nums: List[int]):
        self.notzeros = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.notzeros[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for idx in self.notzeros.keys():
            if idx in vec.notzeros:
                res += self.notzeros[idx] * vec.notzeros[idx]

        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)