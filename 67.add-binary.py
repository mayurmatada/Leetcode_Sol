class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l = int(a, 2)
        m = int(b, 2)
        c = l+m
        return bin(c)[2:]
