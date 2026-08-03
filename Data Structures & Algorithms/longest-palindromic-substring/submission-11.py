class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, -1

        def expand(i1:int, i2:int) -> tuple[int, int]:
            while (i1 >= 0 and i2 < len(s) and 
                    s[i1] == s[i2]):
                    i1, i2 = i1 - 1, i2 + 1
            
            return (i1 + 1, i2 - 1)

        for i, _ in enumerate(s):
            # check odd
            o1, o2 = expand(i, i)
            if o2 - o1 > end - start:
                start, end = o1, o2
            
            #check even
            e1, e2 = expand(i, i+1)
            if e2 - e1 > end - start:
                start, end = e1, e2

        return s[start: end + 1]