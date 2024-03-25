class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        n, m = len(maze), len(maze[0])
        queue = deque([start])
        visited = [start]
        print(visited)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue:
            x, y = queue.popleft()
            if [x, y] == destination:
                # 测试是否可以停住
                for dx, dy in directions: return True

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                while new_x >= 0 and new_x < n and new_y >= 0 and new_y < m and maze[new_x][new_y] == 0:
                    new_x += dx
                    new_y += dy
                new_x -= dx
                new_y -= dy
                if [new_x, new_y] not in visited:
                    queue.append([new_x, new_y])
                    visited.append([new_x, new_y])

        return False
