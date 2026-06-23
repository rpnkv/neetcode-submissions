class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []


        for i_l in range(len(nums) - 2):
            if i_l != 0 and nums[i_l] == nums[i_l-1]:
                continue

            i_m, i_r = i_l + 1, len(nums) - 1
            while i_m < i_r:
                n_l = nums[i_l]
                n_m = nums[i_m]
                n_r = nums[i_r]

                curr_sum = n_l + n_m + n_r
                match curr_sum:
                    case x if x == 0:
                        res.append([n_l, n_m, n_r])
                        i_m += 1
                        while i_m < i_r and nums[i_m] == nums[res[-1][1]]:
                            i_m += 1
                        while i_m < i_r and nums[i_r] == nums[res[-1][2]]:
                            i_r -= 1

                    case x if x < 0:
                        i_m += 1
                    case x if x > 0:
                        i_r -= 1

        return res
