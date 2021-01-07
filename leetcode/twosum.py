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
        nums.sort()
        list_ = []
        # case 1
        # when the 1st digit of sorted array nums is negative
        for j in nums:
            for i in nums:
                if (nums[j] + nums[i]) == target & j!=i:
                    list_.append(j)
                    list_.append(i)
        print(list_)
        return list_
