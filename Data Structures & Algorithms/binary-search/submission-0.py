class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            i_mid = l + ((r - l) // 2)

            match nums[i_mid]:
                case x if x == target:
                    return i_mid
                case x if x < target:
                    l = i_mid + 1
                case _:
                    r = i_mid - 1
        
        return -1