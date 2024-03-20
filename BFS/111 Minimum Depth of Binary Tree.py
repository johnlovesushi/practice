# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        depth = 0
        if not root: return depth

        queue = deque([root])

        while queue:
            depth += 1  # 有这一层的node, 说明有这一层，depth+1

            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if not node.left and not node.right: return depth
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return depth
