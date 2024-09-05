class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # DFS/backtracking: 会超时 42/65
        # 貌似必须结合使用tire才可以
        n, m = len(board), len(board[0])
        output = []

        def dfs(x, y, i, word):
            if i == len(word):
                return True

            if x < 0 or y < 0 or x >= n or y >= m or board[x][y] != word[i]:
                return False

            temp = board[x][y]
            board[x][y] = -1
            res = dfs(x + 1, y, i + 1, word) or dfs(x - 1, y, i + 1, word) or dfs(x, y + 1, i + 1, word) or dfs(x,
                                                                                                                y - 1,
                                                                                                                i + 1,
                                                                                                                word)
            board[x][y] = temp
            return res

        for word in words:
            for i in range(n):
                for j in range(m):
                    if dfs(i, j, 0, word) and word not in output: output.append(word)

        return output
