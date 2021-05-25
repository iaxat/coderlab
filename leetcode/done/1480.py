# Easy

class Solution:
    def runningSum(self, nums):
		# lst = []
        # num = 1
        # while len(lst) != len(nums):
        #     lst.append(sum((nums[0:num])))
        #     num += 1
        # return lst
        new_arr = []
        counter = 0
        for i in nums:
            counter+=i
            new_arr.append(counter)

        print(new_arr)
        return new_arr

nums = [1,2,3,4]
sol = Solution()
sol.runningSum(nums)



# # method 2
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         for i in range(1,len(nums)):
#             nums[i] += nums[i-1]

#         return nums