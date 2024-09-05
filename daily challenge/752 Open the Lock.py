class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        # daily challenge 2024-04-22
        # BFS
        
        if '0000' in deadends: return -1  # 0000 在结果中就没有别的办法了
        visited = set(deadends + ['0000'])

        queue = deque([('0000', 0)])
        step = float("infinity")
        while queue:
            current, idx = queue.popleft()

            if current == target: step = min(step, idx)

            for i in range(4):  # 每个锁有4位数
                # print(len(current),current)
                newlock1 = current[:i] + str((int(current[i]) + 1) % 10) + current[i + 1:]

                newlock2 = current[:i] + ('9' if (int(current[i]) - 1) < 0 else str((int(current[i]) - 1))) + current[
                                                                                                              i + 1:]

                if newlock1 not in visited:
                    queue.append([newlock1, idx + 1])
                    visited.add(newlock1)

                if newlock2 not in visited:
                    queue.append([newlock2, idx + 1])
                    visited.add(newlock2)

        return step if step != float("infinity") else -1