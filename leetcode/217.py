# Easy

from collections import Counter

class Solution():
    def containsDuplicate(self, nums: list[int]) -> bool: # better than 30% solution leetcode
        result = Counter(nums)
        for i in result.keys():
            if result[i] > 1:
                print(True)


    def method_2(self, nums: list[int]) -> bool:
        


nums = [1,1,1,3,3,4,3,2,4,2]
sol = Solution()
sol.containsDuplicate(nums)
