from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suff = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        
        pref = [1] * len(nums)

        for i in range(1, len(nums)):
            pref[i] = pref[i-1] * nums[i-1]

        
        return [p * s for p,s in zip(pref, suff)]
