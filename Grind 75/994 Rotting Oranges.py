class Solution:

    # 需要被优化，速度稍微有点慢
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS 问题
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        n, m = len(grid), len(grid[0])
        visited = set()
        q = deque()

        if grid == [[0]]: return 0
        # 初始化q   - 加入坐标和start_minute as 0
        count = -1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    visited.add((i, j, 0))
        if not q:
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1: return count
            return 0

        while q:
            x, y, minute = q.popleft()
            count = max(count, minute)
            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy
                if new_x >= 0 and new_y >= 0 and new_x < n and new_y < m and (new_x, new_y) not in visited \
                        and grid[new_x][new_y] == 1:
                    q.append((new_x, new_y, minute + 1))
                    grid[new_x][new_y] = 2
                    visited.add((new_x, new_y))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return count
