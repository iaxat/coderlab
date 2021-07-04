class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []
        if len(nums) >=1 and len(nums) <= 1000:
            for i in range(0,len(nums)):
                if nums[i] >=0 and nums[i] <len(nums):
                    ans.append(nums[nums[i]])
        return ans




nums = [0,2,1,5,3,4,5,3,2,56756765756765,23422324234234234234234234]
sol = Solution()
print(sol.buildArray(nums))
