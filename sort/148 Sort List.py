# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def findMid(node):
            slow, fast = node, node
            while fast.next and fast.next.next:  # 这里的条件很重要
                slow = slow.next
                fast = fast.next.next

            return slow

        def merge(head1, head2):
            temp = ListNode(-101)
            curr = temp
            while head1 and head2:
                print(head1.val, head2.val)
                if head1.val < head2.val:
                    curr.next = head1
                    head1 = head1.next
                else:
                    curr.next = head2
                    head2 = head2.next
                curr = curr.next

            if head1:
                curr.next = head1
            if head2:
                curr.next = head2

            return temp.next

        if not head or not head.next:
            return head

        mid = findMid(head)
        # print(mid)
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)
        return merge(left, right)