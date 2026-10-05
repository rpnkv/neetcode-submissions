class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # "can jump" condition: if current N equal or greater than max
        # at each iteration, we update max value with the greates 

        threshold = 0

        for i, n in enumerate(nums):
            if i > threshold:
                return False
            else:
                threshold = max(threshold, i + n)
        
        return True