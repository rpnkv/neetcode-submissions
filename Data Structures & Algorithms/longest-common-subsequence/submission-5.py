class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = {}

        def dfs(i1:int, i2:int) -> None:
            if i1 == len(text1) or i2 == len(text2):
                return 0
            
            if (i1, i2) in res:
                return res[(i1,i2)]

            if text1[i1] == text2[i2]:
                res[(i1,i2)] = 1 + dfs(i1 + 1, i2 + 1)
            else:
                res[(i1,i2)] = max(
                    dfs(i1 + 1, i2), dfs(i1, i2 + 1)
                )
            return res[(i1,i2)]


        dfs(0,0)
        return max(res.values())