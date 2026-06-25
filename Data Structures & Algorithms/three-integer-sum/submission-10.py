class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        triplets = []

        for l in range(len(nums) - 2):

            if l > 0 and nums[l - 1] == nums[l]:
                continue

            m, r = l + 1, len(nums) - 1

            while m < r:
                try:
                    triplet = [nums[l], nums[m], nums[r]]
                except Exception as e:
                    e.add_note(f"l:{l}, m:{m}, r:{r}")
                    raise

                match sum(triplet):
                    case s if s == 0:
                        m += 1
                        while m < r and nums[m] == triplet[1]:
                            m += 1
                        
                        while m < r and nums[r] == triplet[2]:
                            r -= 1
                        triplets.append(triplet)

                    case s if s < 0:
                        m += 1
                    case _:
                        r -= 1

        return triplets

