class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, m = 0, 0
        r = len(nums) - 1

        while m <= r:
            if nums[m] == 0:  # 如果是0的话，那么不需要做什么，继续往下
                nums[m], nums[l] = nums[l], nums[m]
                l += 1
                m += 1
            elif nums[m] == 1:  # 如果是1的话，说明是mid的
                m += 1  # l不需要增加因为可以续集查这个被换过来新的
            else:  # 如果是2的话
                nums[r], nums[l] = nums[l], nums[r]
                r -= 1

        return nums