class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0

        for r, n in enumerate(nums[1:]):
            if n != nums[l]:
                l += 1               
                nums[l] = n
                
        
        return l + 1