class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        indegree = [0] * numCourses
        res = []
        count = 0
        for end, start in prerequisites:
            if start in graph:
                graph[start].append(end)
            else:
                graph[start] = [end]
            indegree[end] += 1

        q = deque()
        # 遍历寻找先修的课
        for i in range(len(indegree)):
            if indegree[i] == 0: q.append(i)  # 这些课程先修

        while q:
            cur = q.popleft()
            count += 1  # 记录上过课程数量
            res.append(cur)  # 记录已经上过的课
            if cur in graph:
                for neighbor in graph[cur]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)

        return res if count == numCourses else []