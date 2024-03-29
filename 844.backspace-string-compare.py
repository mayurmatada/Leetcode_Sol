class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        k = 0
        while(k <= len(s)):
            if (s[k] == '#'):
                s = s[:k-1] + s[k+1:]
                k = k-2
                continue
            k = k+1
                
        i = 0
        while(i <= len(t)):
            if (t[i] == '#'):
                t = t[:i-1] + t[i+1:]
                i = i-2
                continue
            i = i+1
        
        if(t == s):
            return True
        else:
            return False