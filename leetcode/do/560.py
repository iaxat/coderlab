# Medium

class Solution:
    def subarraySum(self, nums,k):
        counter = 0
        sub_dict = {}

        for i in range(len(nums)):
            j = i+1
            for j in range(len(nums)):
                sums = 0
                for i<j:
                    sums+=nums[i]
                    




nums = [1,1,1]
k = 2
sol = Solution()
sol.subarraySum(nums)