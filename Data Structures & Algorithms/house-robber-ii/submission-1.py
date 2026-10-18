class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]

        return max(self.rob_1(nums[0:len(nums) - 1]),
                    self.rob_1(nums[1:len(nums)]))

    def rob_1(self, nums):
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        n = len(nums)
        prev2, prev1 = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            curr = max(prev1, nums[i] + prev2)
            prev2, prev1 = prev1, curr
        
        return prev1
        