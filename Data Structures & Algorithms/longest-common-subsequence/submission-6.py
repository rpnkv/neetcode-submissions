class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp: dict[tuple[int,int], int] = {}

        def dfs(i1: int, i2: int) -> int:
            if i1 == len(text1) or i2 == len(text2):
                return 0
            
            if (i1, i2) in dp:
                return dp[(i1, i2)]
            
            if text1[i1] == text2[i2]:
                dp[(i1, i2)] = dfs(i1 + 1, i2 + 1) + 1
            else:
                dp[(i1,i2)] = max(
                    dfs(i1 + 1, i2),
                    dfs(i1, i2 + 1)
                )
            
            return dp[(i1,i2)]
        
        dfs(0,0)
        return max(dp.values())
                    
