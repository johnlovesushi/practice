class Solution:
    # Apr 3rd 2024
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(x, y, idx):
            # 退出条件
            if idx == len(word):
                return True

            if x < 0 or y < 0 or x >= n or y >= m or board[x][y] == -1:
                return False
            # 检查当前元素是否就是对应idx元素
            if board[x][y] != word[idx]: return False

            # 改变当前元素 防止重复访问
            temp = board[x][y]
            board[x][y] = -1
            # 满足元素
            if dfs(x + 1, y, idx + 1) or dfs(x - 1, y, idx + 1) or dfs(x, y + 1, idx + 1) or dfs(x, y - 1, idx + 1):
                return True
            board[x][y] = temp
            return False

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0): return True

        return False
