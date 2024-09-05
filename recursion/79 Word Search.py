class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n, m = len(board), len(board[0])

        def dfs(x, y, i):
            if i == len(word):
                return True

            if x < 0 or y < 0 or x >= n or y >= m or board[x][y] != word[i]:
                return False

            # 说明board[x][y] == word[i],那么进行下一位的搜索
            temp = board[x][y]
            board[x][y] = -1

            res = dfs(x + 1, y, i + 1) or dfs(x - 1, y, i + 1) or dfs(x, y + 1, i + 1) or dfs(x, y - 1, i + 1)
            board[x][y] = temp
            return res

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0): return True

        return False
