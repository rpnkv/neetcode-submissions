class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [None] * (n + 1)
    
        def dfs(n:int) -> int:
            if n < 3:
                return n
            
            if not dp[n]:
                dp[n] = dfs(n-1) + dfs(n-2)
            
            return dp[n]
        
        return dfs(n)
        