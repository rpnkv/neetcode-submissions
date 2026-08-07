class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        t_c = Counter(t)
        s_c = {}
        l = 0

        min_sub = ""

        def is_match() -> bool:
            if t_c.keys() != s_c.keys():
                return False

            for t_key in t_c:
                if t_c[t_key] > s_c[t_key]:
                    return False

            return True

        for r, char in enumerate(s):
            if char in t_c:
                s_c[char] = s_c.get(char, 0) + 1

            if not is_match():
                continue

            while is_match() and (s[l] not in s_c or s_c[s[l]] > t_c[s[l]]):
                if s[l] in s_c:
                    s_c[s[l]] -= 1

                l += 1

            candidate = s[l:r + 1]
            if min_sub == "" or len(candidate) < len(min_sub):
                min_sub = candidate

        return min_sub
