class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}

        def dfs(i1: int, i2:int) -> int:
            if i1 == len(text1) or i2 == len(text2):
                return 0
            
            if (i1,i2) not in dp:
                res = None
                if text1[i1] == text2[i2]:
                    res = 1 + dfs(i1 + 1, i2 + 1)
                else:
                    res = max(
                        dfs(i1 + 1, i2), dfs(i1, i2 + 1)
                    )
                dp[(i1,i2)] = res
            
            return dp[(i1,i2)]

        return dfs(0,0)
        