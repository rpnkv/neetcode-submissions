class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "#" + "#".join(s) + "#"

        center, rad = 0,0

        for i in range(len(t)):
            curr_rad, l, r = 0, i, i

            while l >= 0 and r < len(t) and t[l] == t[r]:
                curr_rad += 1
                l, r = l - 1, r + 1
            
            curr_rad -= 1

            if curr_rad > rad:
                center, rad = i, curr_rad
        
        s_start = (center - rad) // 2
        return s[s_start: s_start + rad]

            