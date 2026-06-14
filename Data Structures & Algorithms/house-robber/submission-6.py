class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(n: int, dp) -> int:
            if n >= len(nums):
                return 0
            else:
                if not dp[n]:
                    dp[n] = nums[n] + max(
                        dfs(n + 2, dp), dfs(n+3, dp)
                    )

                return dp[n]

        dp0: list[None | int] = [None] * len(nums)
        dp1: list[None | int] = [None] * len(nums)

        dfs0 = dfs(0, dp0)
        dfs1 = dfs(1, dp1)

        return max(dfs0, dfs1)
