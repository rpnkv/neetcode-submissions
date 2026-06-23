class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []


        for i_l in range(len(nums) - 2):
            i_m, i_r = i_l + 1, len(nums) - 1
            while i_m < i_r:
                n_l = nums[i_l]
                n_m = nums[i_m]
                n_r = nums[i_r]

                curr_sum = n_l + n_m + n_r
                match curr_sum:
                    case x if x == 0:
                        res.append([nums[i_l], nums[i_m], nums[i_r]])

                        i_m += 1
                        i_m += 1
                        while i_m < i_r and nums[i_m] == nums[i_m - 1]:
                            i_m += 1

                        # Сдвигаем r влево, пропуская дубликаты
                        i_r -= 1
                        while i_m < i_r and nums[i_r] == nums[i_r + 1]:
                            i_r -= 1
                    case x if x < 0:
                        i_m += 1
                    case x if x > 0:
                        i_r -= 1

        return res