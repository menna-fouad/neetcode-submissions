class Solution:
    def reverseBits(self, n: int) -> int:
        res = ((n & 0xFFFF0000) >> 16) | ((n & 0x0000FFFF) << 16)
        res = ((res & 0xFF00FF00) >> 8) | ((res & 0x00FF00FF) << 8)
        res = ((res & 0xF0F0F0F0) >> 4) | ((res & 0x0F0F0F0F) << 4)
        res = ((res & 0xCCCCCCCC) >> 2) | ((res & 0x33333333) << 2)
        res = ((res & 0xAAAAAAAA) >> 1) | ((res & 0x55555555) << 1)
        
        return res
        