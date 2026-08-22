class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        
        dp = [None] * (len(nums))
        dp[0], dp[1], dp[2] = nums[0], nums[1], nums[2] + nums[0]

        def dfs(i: int) -> int:
            if not dp[i]:
                dp[i] = max(
                    dp[i - 2],
                    dp[i - 3]
                ) + nums[i]
            
            return dp[i]
        
        dfs(len(nums) - 1)
        dfs(len(nums) - 2)
        return max(dp[-1], dp[-2])
