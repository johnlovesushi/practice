class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        indegree = [0] * numCourses
        for end, start in prerequisites:
            if start in graph:
                graph[start].append(end)
            else:
                graph[start] = [end]
            indegree[end] += 1
        print(graph)
        q = deque()
        count = 0  # 计数上过多少门课
        for i in range(len(indegree)):
            if indegree[i] == 0: q.append(i)
        while q:
            cur = q.popleft()
            count += 1
            if cur in graph:
                for neighbor in graph[cur]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)

        return count == numCourses

