class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()

        def result() -> list[int]:
            return [nums[l], nums[m], nums[r]]

        for l in range(len(nums) - 2):
            m, r = l + 1, len(nums) - 1
            while m < r:
                n_l = nums[l]
                n_m = nums[m]
                n_r = nums[r]

                curr_sum = n_l + n_m + n_r
                if curr_sum == 0:
                    duplicate = False

                    for prev_l, prev_m, prev_r in reversed(results):
                        if prev_l != n_l:
                            break

                        if prev_m == n_m:
                            duplicate = True
                            break

                    if not duplicate:
                        results.append(result())

                    m += 1

                if sum(result()) > 0:
                    r -= 1
                else:
                    m += 1

        return results