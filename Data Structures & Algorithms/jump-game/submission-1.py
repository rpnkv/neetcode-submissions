class Solution:
    def canJump(self, nums: List[int]) -> bool:
        thrshold = 1

        for i, n in nums:
            if i >= threshold:
                threshold = max(threshold, i + n)
            else:
                return False

        return True