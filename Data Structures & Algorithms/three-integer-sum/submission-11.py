class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        
        for l in range(len(nums) - 2):
            if l > 0 and nums[l - 1] == nums[l]:
                continue

            m, r = l + 1, len(nums) - 1

            while m < r:
                match nums[l] + nums[m] + nums[r]:
                    case s if s == 0:
                        res.append([nums[l], nums[m], nums[r]])
                        while m < r and nums[m] == res[-1][1]:
                            m += 1

                        while m < r and nums[r] == res[-1][2]:
                            r -= 1

                    case s if s < 0:
                        m += 1
                    case s if s > 0:
                        r -= 1

        
        return res
