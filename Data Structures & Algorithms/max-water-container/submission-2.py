class Solution:
    def maxArea(self, height: List[int]) -> int:
        nums = height
        l, r = 0, len(height) - 1

        max_area = 0

        while l < r:
            area = (r - l) * min(nums[l], nums[r]) 

            max_area = max(area, max_area)

            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1

        return max_area