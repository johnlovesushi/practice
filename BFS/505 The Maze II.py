class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        n, m = len(maze), len(maze[0])  # row_num, col_num
        distance = [[float("infinity") for i in range(m)] for j in range(n)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        distance[start[0]][start[1]] = 0  # 启示为0
        pq = [(distance, start[0], start[1])]

        while pq:
            dist, x, y = heapq.heappop(pq)

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                count = 0
                while new_x >= 0 and new_y >= 0 and new_x < n and new_y < m and maze[new_x][new_y] == 0:
                    new_x += dx
                    new_y += dy
                    count += 1
                new_x -= dx
                new_y -= dy

                if distance[x][y] + count < distance[new_x][new_y]:
                    distance[new_x][new_y] = distance[x][y] + count
                    heapq.heappush(pq, (distance[new_x][new_y], new_x, new_y))

        return distance[destination[0]][destination[1]] if distance[destination[0]][destination[1]] != float(
            "infinity") else -1                