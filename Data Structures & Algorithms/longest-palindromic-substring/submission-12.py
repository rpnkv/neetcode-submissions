class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "#" + "#".join(s) + "#"

        best_center, best_radius = 0, 1

        for i, _ in enumerate(t):
            radius = 0
            l = r = i

            while l >= 0 and r < len(t) and t[l] == t[r]:
                radius += 1
                l, r = l - 1, r + 1
            radius -= 1
            
            if radius > best_radius:
                best_center, best_radius = i, radius
        
        start = (best_center - best_radius) // 2
        return s[start: start + best_radius]

            