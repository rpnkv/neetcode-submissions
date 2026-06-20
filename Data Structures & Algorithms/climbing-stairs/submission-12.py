from functools import lru_cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(n: int) -> int:
            if n <= 2:
                return n
            return dfs(n-1) + dfs(n-2)
        return dfs(n)