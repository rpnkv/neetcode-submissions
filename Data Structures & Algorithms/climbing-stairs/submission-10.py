class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [None] * (n + 1)
        dp[1], dp[2] = 1,2

        def dfs(n: int) -> int:
            if not dp[n]:
                dp[n] = dfs(n-1) + dfs(n-2)
            
            return dp[n]
        
        return dfs(n)
                