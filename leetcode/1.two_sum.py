# Two Sum Question
# Difficulty: Easy
# Leetcode Problem Section

# The program needs to find the index of the values inside the nums list,
# which can sum together to equalte the value of target
# three cases defined in this problem which can make it smaller 
# in compare to other methods

# method 1
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        list_ = []
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j] == target) :
                    list_.append(j)
                    list_.append(i)
                    return list_
