class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []

        for k in range(len(nums)):
            if nums[k] > 0: break
            if k > 0 and nums[k] == nums[k - 1]: continue

            i, j = k + 1, len(nums) - 1

            while i < j:
                
                sum = nums[i] + nums[j] + nums[k]
                if sum > 0: j -= 1
                elif sum < 0: i += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        
        return res
