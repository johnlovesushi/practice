class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stk = []

        operators = set(['+', '-', '*', '/'])

        for token in tokens:
            if token in operators:
                second_num = stk.pop()
                first_num = stk.pop()

                if token == '+':
                    total = first_num + second_num
                elif token == '-':
                    total = first_num - second_num
                elif token == '*':
                    total = first_num * second_num
                else:
                    total = int(first_num / second_num)

                stk.append(total)
            else:  # 说明是数字
                stk.append(int(token))  # 直接使用int就可以直接转化成正数或者是负数

                # 方法二： string type的数值转化成 int
                # num = 0
                # sign = 1
                # for i in range(len(token)):
                #         if i ==0 and token[i] == '-':
                #             sign = -1
                #         else: num = num * 10 + int(token[i])
                # stk.append(sign*num)

        return stk[-1]
