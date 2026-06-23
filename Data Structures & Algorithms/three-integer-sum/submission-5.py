class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []


        for l in range(len(nums) - 2):
            m, r = l + 1, len(nums) - 1
            while m < r:
                curr_sum = nums[l] + nums[m] + nums[r]
                match curr_sum:
                    case x if x == 0:
                        if not res or not (res[-1][0] == nums[l] and res[-1][1] == nums[m]):
                            res.append([nums[l], nums[m], nums[r]])

                        m += 1
                    case x if x < 0:
                        m += 1
                    case x if x > 0:
                        r -= 1

        return res