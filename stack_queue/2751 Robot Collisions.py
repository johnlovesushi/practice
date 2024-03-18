class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stk = []
        pos = []
        res = []
        idx = [i for i in range(len(positions))]
        for pos, health, direction, idx in sorted(zip(positions, healths, directions, idx)):
            while stk and stk[-1][2] == 'R' and direction == 'L':  # 发生碰撞
                if stk[-1][1] == health:  # 同样健康，直接两个都报废
                    stk.pop()
                    break
                elif stk[-1][1] < health:  # 继续查验碰撞是否左边的
                    health -= 1
                    stk.pop()
                else:  # 右边的报废，左边的健康-1
                    stk[-1][1] -= 1
                    break
            else:
                stk.append([pos, health, direction, idx])

        for _, health, _, _ in sorted(stk, key=lambda x: x[3]):
            res.append(health)
        return res