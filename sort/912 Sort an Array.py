class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def partition(nums, left, right):
            pivot = nums[right]  # 用pivot来表示数， right来表示index
            pivot = left + int(random.random() * (right - left + 1))
            start = left
            end = right - 1
            while start <= end:
                if nums[start] <= pivot:
                    start += 1
                elif nums[end] > pivot:
                    end -= 1
                else:  # 说明pivot左边的元素比pivot大，或者pivot右边的元素比pivot小
                    nums[start], nums[end] = nums[end], nums[start]
                    start += 1
                    end -= 1
            nums[start], nums[right] = nums[right], nums[start]  # 把pivot交换到应该的位置

            return start  # 相当于return pivot

        def helper(nums, left, right):
            if left >= right: return

            pivot = partition(nums, left, right)
            helper(nums, left, pivot - 1)
            helper(nums, pivot + 1, right)
            return

        # 尝试打算
        random.shuffle(nums)  # testcase里面有最差情况，需要打乱
        helper(nums, 0, len(nums) - 1)
        return nums