class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""

        l = 0
        win_set = set()

        for r, c in enumerate(s):
            if not win_set:
                l = r

            if c in t:
                win_set.add(c)

            if win_set == set(t):
                if r - l - 1 < len(res) or res == "":
                    res = s[l:r + 1]

                win_set.remove(s[l])
                l += 1

                while l <= r and s[l] not in win_set:
                    l += 1

        return res