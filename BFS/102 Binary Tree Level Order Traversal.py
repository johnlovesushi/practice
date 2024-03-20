# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root: return res
        queue = deque([root])

        while queue:
            temp = []
            n = len(queue)  # 确定这一层有多少node, 其他后加入的都不是这一层的
            for i in range(n):
                node = queue.popleft()  # pop出来
                temp.append(node.val)  # 然后append
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(temp)

        return res
