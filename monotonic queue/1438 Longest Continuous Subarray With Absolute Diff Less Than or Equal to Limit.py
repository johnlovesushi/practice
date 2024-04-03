class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increase_stack = deque()
        decrease_stack = deque()
        left = 0
        res = 0
        for i in range(len(nums)):
            while increase_stack and nums[i] > increase_stack[-1]:
                increase_stack.pop()
            while decrease_stack and nums[i] < decrease_stack[-1]:
                decrease_stack.pop()

            increase_stack.append(nums[i])
            decrease_stack.append(nums[i])

            if increase_stack[0] - decrease_stack[0] > limit:  # 超过了限制
                if increase_stack[0] == nums[left]:
                    increase_stack.popleft()
                if decrease_stack[0] == nums[left]:
                    decrease_stack.popleft()
                left += 1

        return len(nums) - left