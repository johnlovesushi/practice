class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:

        # lazy addition
        # 其实就是标记好需要加的开始index，然后再标记好一个end的index减去那个值，最后rolling sum就可以了
        res = [0] * length
        for start, end, val in updates:
            res[start] += val
            if end + 1 < len(res):
                res[end + 1] -= val

        prefixsum = 0
        for i in range(len(res)):
            prefixsum += res[i]
            res[i] = prefixsum

        return res