class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        # method 1: 速度不够快 可以优化
        if "0000" in deadends: return -1
        queue = deque([("0000", 0)])
        visited = set(deadends + ['0000'])
        step = float("infinity")  # 如果最后step还是infinity, 那么就return -1

        while queue:
            num, temp_step = queue.popleft()
            # print(num,temp_step)
            if num == target: step = min(step, temp_step)
            for i in range(4):  # 重组新的数值
                new_num1 = num[:i] + str((int(num[i]) + 1) % 10) + num[i + 1:]
                new_num2 = num[:i] + str(9 if (int(num[i]) - 1) < 0 else int(num[i]) - 1) + num[i + 1:]
                new_step = temp_step + 1
                if new_num1 not in visited:
                    queue.append((new_num1, new_step))
                    visited.add(new_num1)  # 需要加入queue的时候就加入visited, 要不然还是能压入很多重复的组合

                if new_num2 not in visited:
                    queue.append((new_num2, new_step))
                    visited.add(new_num2)  # 需要加入queue的时候就加入visited, 要不然还是能压入很多重复的组合

        return step if step != float("infinity") else -1


