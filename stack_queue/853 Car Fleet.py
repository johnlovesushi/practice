class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []

        for pos, spd in sorted(zip(position, speed), reverse=True):
            time = (target - pos) / spd

            if not stk or stk[-1] < time:
                stk.append(time)

        return len(stk)
