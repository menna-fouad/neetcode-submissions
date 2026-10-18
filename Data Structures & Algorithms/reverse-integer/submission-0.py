class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2 ** 31
        MAX = 2 ** 31 - 1

        res = 0

        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if res > (MAX - digit) // 10:
                return 0
            
            if res < int((MIN - digit) / 10):
                return 0
            
            res = res * 10 + digit
        
        return res
        