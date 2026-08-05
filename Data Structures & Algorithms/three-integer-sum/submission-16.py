class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for l in range(len(nums) - 3):
            if nums[l] > 0:
                break

            if l > 0 and nums[l - 1] == nums[l]:
                continue
            
            m, r = l + 1, len(nums) - 1

            while m < r:
                match nums[l] + nums[m] + nums[r]:
                    case s if s == 0:
                        res.append([nums[l], nums[m], nums[r]])
                        m, r = m + 1, r - 1

                        while m < r and nums[res[-1][1]] == nums[m]:
                            m += 1
                        
                        while m < r and nums[res[-1][2]] == nums[r]:
                            r -= 1

                    case s if s < 0:
                        m += 1
                    case s if s > 0:
                        r -= 1

        return res
                