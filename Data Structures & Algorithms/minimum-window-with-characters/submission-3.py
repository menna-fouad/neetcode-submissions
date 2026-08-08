class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars_T = {}
        window = {}

        for char in t:
            chars_T[char] = chars_T.get(char, 0) + 1
        
        have = 0
        need = len(chars_T)
        l = 0

        idx = [-1, -1]
        length = float('inf')

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in chars_T and window[s[r]] == chars_T[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < length:
                    idx = [l, r]
                    length = r - l + 1
                
                window[s[l]] -=1
                if s[l] in chars_T and window[s[l]] < chars_T[s[l]]:
                    have -= 1
                
                l += 1
        
        return s[idx[0] : idx[1] + 1] if length != float('inf') else ''
