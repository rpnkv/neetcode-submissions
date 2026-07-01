class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        longest = 0

        for n in nums:
            if n - 1 in s:
                continue
            
            current = 1 
            while n + 1 in s:
                n, current = n + 1, current + 1
            
            longest = max(current, longest)

        return longest