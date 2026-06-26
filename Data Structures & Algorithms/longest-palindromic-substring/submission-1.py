class Solution:
    def longestPalindrome(self, s: str) -> str:
        # works for odd lists only
        m = ""

        def check_pal(l: int, r: int) -> tuple(bool, tuple[int, int]):
            if l < 0 or r > len(s):
                return (False, (0, 0))

            pal_l, pal_r = l, r

            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                pal_l, pal_r = l, r

                l -= 1
                r += 1

            return ((pal_l, pal_r) != (l, r), (pal_l, pal_r))

        for i in range(len(s)):
            # check odd
            l, r = i, i + 1
            odd_check = check_pal(l, r)
            if odd_check[0]:
                o_l, o_r = odd_check[1]
                if len(m) < (o_r - o_l + 1):
                    m = s[o_l:o_r + 1]

            # check even
            l, r = i - 1, i + 1
            even_check = check_pal(l, r)
            e_l, e_r = even_check[1] if even_check else (i, i)
            if len(m) < (e_r - e_l + 1):
                m = s[e_l:e_r + 1]

        return m