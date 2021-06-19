# Hard

class Solution():
    def airbub(self,nums):
        result1 = 0
        result2 = 0
        for i in range(0,len(nums)):
            if i % 2 == 0:
                result1 += nums[i]
            else:
                result2 += nums[i]
        return max(result1,result2)


nums = [2, 4, 6, 2, 5]
sol = Solution()
sol.airbub(nums)
