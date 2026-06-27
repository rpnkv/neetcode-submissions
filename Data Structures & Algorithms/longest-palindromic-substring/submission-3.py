class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pal = (0, -1)  # когда такое не проканает?

        def check_for_pal(l, r) -> tuple[bool, int, int]:
            l_pal, r_pal = l, r
            is_pal = l == r

            while l >= 0 and r <= len(s) - 1:
                if s[l] == s[r]:
                    is_pal = True
                    l_pal, r_pal = l, r

                l -= 1
                r += 1

            return (is_pal, l_pal, r_pal)

        for i, _ in enumerate(s):
            is_pal, l_even, r_even = check_for_pal(i, i)
            if is_pal and (max_pal[1] - max_pal[0]) < (r_even - l_even):
                max_pal = (l_even, r_even)

            is_pal, l_odd, r_odd = check_for_pal(i, i + 1)
            if is_pal and (max_pal[1] - max_pal[0]) < (r_odd - l_odd):
                max_pal = (l_odd, r_odd)

        return s[max_pal[0]: max_pal[1] + 1]
