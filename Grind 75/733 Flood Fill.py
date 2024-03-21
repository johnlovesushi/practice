class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        oldcolor = image[sr][sc]
        n, m = len(image), len(image[0])
        queue = deque([(sr, sc)])
        visited = set()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while queue:
            r, c = queue.popleft()
            image[r][c] = color
            visited.add((r, c))
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if new_r >= 0 and new_r < n and new_c >= 0 and new_c < m and (new_r, new_c) not in visited and \
                        image[new_r][new_c] == oldcolor:
                    queue.append((new_r, new_c))

        return image

