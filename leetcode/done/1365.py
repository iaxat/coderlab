# Easy

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        # result = []
        
        # for i in range(len(nums)):
        #     counter = 0
        #     for j in range(len(nums)):
        #         if i!= j:
        #             if nums[j]<nums[i]:
        #                 counter+=1
        #     result.append(counter)

        # print(result)
        # return result


        # method 2
        nums = sorted(nums)
        print(nums)
        

nums = [8,1,2,2,3]
sol = Solution()
sol.smallerNumbersThanCurrent(nums)