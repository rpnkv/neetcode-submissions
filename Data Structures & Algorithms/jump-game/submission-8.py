class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_available = 0

        for i, n in enumerate(nums):
            if i <= max_available:
                max_available = max(max_available, i + n)
            else:
                return False
        
        return True