class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = []
        paths.append([1] * m)

        for i_n in range(1, n):
            prev = paths[-1]
            current = [-1] * m
            for i_m in range(m):
                prev_top = prev[i_m]
                prev_left = 0 if i_m == 0 else current[i_m - 1]
                current[i_m] = prev_top + prev_left

            paths.append(current)



        return paths[-1][-1]