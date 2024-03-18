class Solution:
    def countCollisions(self, directions: str) -> int:
        """
        LR： 不会撞车，\ /
        RL： 撞车， / \
        RS： 撞车： /｜ 并且如果前面有任何Rturn的车，都会撞成｜
        SL： 撞车： ｜\ ，直接L撞成｜
        :param directions:
        :return:
        """
        stk = []
        stk.append(directions[0])
        collision = 0
        for i in range(1, len(directions)):
            curr = directions[i]
            if stk[-1] == 'R' and curr == 'L':
                collision += 2
                stk.pop()
                curr = 'S'
            elif stk[-1] == 'S' and curr == 'L':
                collision += 1
                curr = 'S'
            while stk and stk[-1] == 'R' and curr == 'S':
                stk.pop()
                collision += 1

            stk.append(curr)

        return collision