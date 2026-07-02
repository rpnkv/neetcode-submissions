class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0

        for i, n in enumerate(nums):
            if max_index >= i:
                max_index = max(max_index, i + n)
            else:
                return False

        return True