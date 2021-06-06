
class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        sorted_nums = sorted(nums,reverse=True)
        result = 0
        stacks = []
        if len(nums)>=1 and len(nums)<=5*10**4:
            condition = len(nums)*min(nums)
            if sum(nums) > condition:
                for i in range(len(sorted_nums)):
                    if i+1<len(sorted_nums):
                        if sorted_nums[i] not in stacks:
                            stacks.append(sorted_nums[i])
                sorted_nums = stacks
                print(sorted_nums)
                for j in range(len(sorted_nums)-1):
                    while sorted_nums[j] in nums:
                        ind = nums.index(sorted_nums[j])
                        nums[ind] = sorted_nums[j+1]
                        result+=1
        return result

nums = [5,1,3]
sol = Solution()
print(sol.reductionOperations(nums))