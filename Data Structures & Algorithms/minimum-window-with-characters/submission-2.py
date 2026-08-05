class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start, ln = 0, 0
        l = 0
        win, allowed = {}, set(t)

        for r, char in enumerate(s):
            if char in allowed:
                win[char] = 1 + win.get(char, 0)

            #while len(win) == len(allowed) and any((cnt > 1 for cnt in win.values())):
            while len(win) == len(allowed):
                if s[l] in allowed:
                    if win[s[l]] > 1:
                        win[s[l]] -= 1
                    else:
                        break
                l += 1
            
            if len(win) == len(allowed):
                if ln == 0 or r - l + 1 < ln:
                    start, ln = l, r - l + 1
        
        return s[start: start + ln]