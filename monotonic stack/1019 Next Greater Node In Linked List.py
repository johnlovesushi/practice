# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        res = []
        stack = []
        curr = head

        # 得先reverse the linklist

        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        curr = prev
        while curr:
            while stack and stack[-1] <= curr.val: stack.pop()
            res.append(0 if not stack else stack[-1])
            stack.append(curr.val)
            curr = curr.next

        # 转回来

        return res[::-1]