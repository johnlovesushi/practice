class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # method 1: quick sort的方法过不了 40/41
        # n = len(nums)
        # def partition(nums,left,right):
        #     pivot_index = random.randint(left, right)
        #     nums[pivot_index], nums[right] = nums[right], nums[pivot_index]     # 必须先和right替换
        #     pivot = nums[right]
        #     start = left
        #     end = right - 1
        #     while start <= end:
        #         if nums[start] <= pivot: start+=1
        #         elif nums[end] > pivot: end-=1
        #         else:
        #             nums[start],nums[end] = nums[end],nums[start]
        #             start+=1
        #             end-=1
        #     nums[start],nums[right] = nums[right],nums[start]
        #     return start

        # def helper(nums,left,right):
        #     if left >= right: return
        #     position = partition(nums,left,right)

        #     if position == n - k: return
        #     elif position > n-k:  # 说明pivot的位置过大
        #         helper(nums,left, position-1)
        #     else:
        #         helper(nums,position+1,right)

        # #random.shuffle(nums)
        # helper(nums,0,len(nums)-1)
        # return nums[n-k]

        # method 2： 直接sort完取就可以了
        return sorted(nums)[-k]