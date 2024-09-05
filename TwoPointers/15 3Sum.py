class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]: continue

            target = -nums[i]
            l, r = i + 1, len(nums) - 1

            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[l], nums[r], -target])
                    l += 1
                    while l <= r and nums[l] == nums[l - 1]:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1

        return res