class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # l = 0
        # r = len(nums) - 1

        # while l<= r:
        #     m = l+(r-l)//2
        #     if nums[m] == target: return m
        #     elif nums[m] > target:
        #         r = m-1
        #     else:
        #         l = m+1

        # return -1

        def BinarySearch(l, r, nums, target):
            # print()
            if l > r: return -1

            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                return BinarySearch(l, m - 1, nums, target)
            else:
                return BinarySearch(m + 1, r, nums, target)

        return BinarySearch(0, len(nums) - 1, nums, target)