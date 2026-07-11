class Solution:
    def canJump(self, nums: List[int]) -> bool:
        threshold = 1

        for i, n in enumerate(nums):
            if i >= threshold:
                threshold = max(threshold, i + n)
            else:
                return False

        return True