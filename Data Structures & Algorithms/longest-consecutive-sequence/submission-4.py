class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        l = 0
        curr_len = max_len = 1 if nums else 0

        for r in range(1, len(nums)):
            if nums[l] == nums[r]:
                pass
            else:
                if nums[r] == nums[l] + 1:
                    curr_len += 1
                else:
                    curr_len = 1    
                l = r
                max_len = max(curr_len, max_len)
        
        return max_len

