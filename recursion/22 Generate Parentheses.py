class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # backtracking
        res = []
        temp = []

        def dfs(open, close, n):
            # print(open,close)
            # [0,0],[1,0],[2,0],[3,0],[3,1],[3,2],[3,3] => ((()))
            # 会一直退回[2,0], 然后[2,1],[3,1],[3,2],[3,3] => (()())
            if open == n and close == n:
                res.append("".join(temp.copy()))
                return

            if open < n:  # 最多可以到n
                temp.append('(')
                dfs(open + 1, close, n)
                temp.pop()

            if close < open:
                temp.append(')')
                dfs(open, close + 1, n)
                temp.pop()

        dfs(0, 0, n)
        return res



