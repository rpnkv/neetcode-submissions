class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mem = {}

        def dfs(i1: int, i2: int) -> int:
            if i1 == len(text1) or i2 == len(text2):
                return 0

            # for i in range(i1, len(text1)):
            #     for j in range(i2, len(text2)):
            #         if text1[i] == text2[j]:
            #             if not (i, j) in mem:
            #                 max_len = max(dfs(i1 + 1, i2 + 1) + 1, 1)
            #                 mem[(i, j)] = max(mem.get((i, j), 0), max_len)
            #
            # return mem.get((i1, i2), 0)
            if (i1, i2) in mem:
                return mem[(i1, i2)]

            if text1[i1] == text2[i2]:
                mem[(i1, i2)] = dfs(i1 + 1, i2 + 1) + 1
            else:
                mem[(i1, i2)] = max(dfs(i1, i2 + 1), dfs(i1 + 1, i2))

            return mem[(i1, i2)]

        dfs(0, 0)
        return max(mem.values())