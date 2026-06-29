class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {1:1, 2:2}

        def dfs(n:int) -> int:
            match n:
                case x if x < 1:
                    return 0
                case x if x < 3:
                    return dp[x]
                case x if not x in dp:
                    dp[x] = dfs(x - 1) + dfs(x - 2)
                    return dp[x]
                case _:
                    return dp[x]

        return dfs(n)