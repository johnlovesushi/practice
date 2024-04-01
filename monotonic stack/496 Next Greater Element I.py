class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = {}

        for i in range(len(nums2) - 1, -1, -1):
            # 单调递增的monotonic stack, 如果stack最上面的元素还是小于nums[i], 那么就pop
            while stack and stack[-1] < nums2[i]: stack.pop()
            hashmap[nums2[i]] = -1 if not stack else stack[-1]
            stack.append(nums2[i])

        res = [0] * len(nums1)

        for i in range(len(res)):
            res[i] = hashmap[nums1[i]]

        return res