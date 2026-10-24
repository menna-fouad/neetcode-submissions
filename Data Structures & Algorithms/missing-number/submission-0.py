class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = 0
        actual = 0

        for i in range(len(nums)):
            expected ^= i
            actual ^= nums[i]
        
        expected ^= len(nums)
        return expected ^ actual
        