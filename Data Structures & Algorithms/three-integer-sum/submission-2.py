class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()

        def result() -> list[int]:
            return [nums[l], nums[m], nums[r]]

        for l in range(len(nums) - 2):
            m, r = l + 1, len(nums) - 1
            while m < r:
                if sum(result()) == 0:
                    results.append(result())
                    break

                if sum(result()) > 0:
                    r -= 1
                else:
                    m += 1

        return results

