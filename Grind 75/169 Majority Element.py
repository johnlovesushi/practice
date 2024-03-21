class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # method 1
        nums.sort()
        count = 1
        n = len(nums)

        for i in range(1,n):
            if nums[i] == nums[i-1]:
                count+=1
            else:
                if count >= n//2 + 1: return nums[i-1]
                count = 1

        return nums[-1]
        
        # method 2
        count = Counter(nums)
        n = len(nums)
        for key, val in count.items():
            if val >= n // 2 + 1: return key

        return -1