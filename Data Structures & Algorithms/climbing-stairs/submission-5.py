class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        prev2, prev1 = 1, 2
        for i in range(2, n):
            curr = prev1 + prev2
            prev2, prev1 = prev1, curr
        
        return prev1
        