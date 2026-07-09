class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ln: list[None | int] = [None] * len(text1)
        ln_max = 0

        for i, c1 in enumerate(text1):
            for j, c2 in enumerate(text2):
                if c1 == c2:
                    ln[i] = 1
                    for i1 in range(i - 1, -1, -1):
                        if ln[i1]:
                            ln[i] = max(ln[i1] + 1, ln[i])

                    ln_max = max(ln_max, ln[i])

        return ln_max
