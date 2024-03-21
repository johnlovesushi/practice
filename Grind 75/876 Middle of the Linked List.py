# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        # 其实就是快慢指针，使用fast and fast.next有可能就是到fast这里就已经是None, 那么就不可能有fast.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
