class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = max_len = zeroes = 0

        for r, num in enumerate(nums):
            if num == 0:
                zeroes += 1

            while zeroes > k:
                if nums[l] == 0:
                    zeroes -= 1
                l+=1

            max_len = max(max_len, r - l + 1)

        return max_len            
