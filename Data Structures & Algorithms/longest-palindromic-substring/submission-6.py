class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_l, max_r = 0, 0

        def check_pal(l: int, r: int) -> tuple[int, int]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1

            return (l + 1, r - 1)

        for i, _ in enumerate(s):
            # check even
            e_l, e_r = check_pal(i, i + 1)
            if e_r - e_l > max_r - max_l:
                max_l, max_r = e_l, e_r
            
            # check odd
            o_l, o_r = check_pal(i, i)
            if max_r - max_l < o_r - o_l:
                max_l, max_r = o_l, o_r
        
        return s[max_l: max_r + 1]

