# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0

    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root: return 2  # 如果2个都return是2那么说明是没有被cover的leaf,
            left = dfs(root.left)
            right = dfs(root.right)
            if left == 2 and right == 2:  # 说明自己是一个leaf,并且没有被cover
                return 0
            if left == 0 or right == 0:  # 说明这个node的左右leaf有没有被cover的，那么这里必须设置一个camera
                self.res += 1
                return 1
            if left == 1 or right == 1:  # 说明子leaf已经被cover,并且当前node也被当作parent node cover了，但上面的node没有被cover
                return 2
            return -1000

        # res = 0

        return (1 if dfs(root) < 1 else 0) + self.res

