class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        count = 0
        visited = set()
        n, m = len(grid), len(grid[0])
        # 使用BFS: 会超时
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j] == "1" and (i,j) not in visited:
        #             count+=1
        #             q = deque([(i,j)])
        #             #print(q)
        #             while q:
        #                 x,y = q.popleft()
        #                 visited.add((x,y))
        #                 for dx,dy in dirs:
        #                     new_x = x + dx
        #                     new_y = y + dy

        #                     if new_x >=0 and new_y >=0 and new_x < n and new_y < m and grid[new_x][new_y] == "1" \
        #                     and (new_x,new_y) not in visited:
        #                         q.append((new_x,new_y))

        # method 2: DFS 不会超时
        def dfs(x, y):
            if x < 0 or y < 0 or x >= n or y >= m or (x, y) in visited or grid[x][y] == "0":
                return

            visited.add((x, y))

            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy
                dfs(new_x, new_y)
            return

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count += 1
                    dfs(i, j)
        return count
