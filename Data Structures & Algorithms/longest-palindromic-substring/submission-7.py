class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_start, max_end = 0, -1

        def check_pal(l:int, r:int) -> tuple[int,int]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            
            return (l + 1,r - 1)

        def check_if_longer(l: int, r: int) -> None:
            nonlocal max_start, max_end
            if (r - l) > (max_end - max_start):
                max_start, max_end = l, r

        for i, char in enumerate(s):
            # check odd
            longest_odd = check_pal(i, i)
            check_if_longer(*longest_odd)

            longest_even = check_pal(i, i + 1)
            check_if_longer(*longest_even)

        return "".join(s[max_start: max_end + 1])