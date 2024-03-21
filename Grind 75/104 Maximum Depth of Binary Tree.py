# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # 典型 BFS，其实也可以把depth 放进queue里面，每一次pop出来+1
        depth = 0
        if not root: return 0
        queue = deque([root])

        while queue:
            depth += 1
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return depth
