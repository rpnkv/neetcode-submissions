class Solution:
    def rob(self, nums: List[int]) -> int:

        results = []
        # ex_X: 0(2)=2; 1(1)=1; 2(1)=3; 3(2)=4

        for i in range(len(nums)):
            prev_1 = prev_2 = 0

            if i - 2 >= 0:
                prev_1 = results[i-2]

            if i - 3 >= 0:
                prev_2 = results[i-3]

            results.append(max(prev_1, prev_2) + nums[i])
        return max(results[-1], results[-2]) if len(results) > 1 else results[0]
