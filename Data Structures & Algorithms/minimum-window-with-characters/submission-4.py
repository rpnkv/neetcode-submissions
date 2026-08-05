class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        start, ln = 0, 0
        l = 0
        win, allowed = {}, Counter(t)

        def if_all_chars() -> bool:
            if win.keys() != allowed.keys():
                return False

            for win_key in win:
                if win[win_key] < allowed[win_key]:
                    return False
            return True

        for r, char in enumerate(s):
            if char in allowed:
                win[char] = 1 + win.get(char, 0)

            #while len(win) == len(allowed) and any((cnt > 1 for cnt in win.values())):
            while if_all_chars():
                if s[l] in allowed:
                    if win[s[l]] > allowed[s[l]]:
                        win[s[l]] -= 1
                    else:
                        break
                l += 1

            if if_all_chars():
                if ln == 0 or r - l + 1 < ln:
                    start, ln = l, r - l + 1

        return s[start: start + ln]