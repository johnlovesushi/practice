class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stk = []

        for asteroid in asteroids:
            while stk and stk[-1] > 0 and asteroid < 0:  # 不同方向, 需要考虑左右
                if abs(stk[-1]) < abs(asteroid):
                    stk.pop()
                elif abs(stk[-1]) > abs(asteroid):
                    break
                else:
                    stk.pop()
                    break
            else:  # 说明同方向或者空集
                stk.append(asteroid)
        return stk

