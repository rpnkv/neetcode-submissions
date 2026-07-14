class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s, max_len = set(nums), 0

        for n in nums:
            if n - 1 in s:
                continue
            else:
                curr_len = 1
                while n + 1 in s:
                    curr_len, n = curr_len + 1, n + 1
                
                max_len = max(max_len, curr_len)
        
        return max_len