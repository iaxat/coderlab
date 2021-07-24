# Easy

from collections import Counter

class Solution():
    def containsDuplicate(self, nums: list[int]) -> bool: # better than 30% solution leetcode
        result = Counter(nums)
        for i in result.keys():
            if result[i] > 1:
                return True


    def method_2(self, nums: list[int]) -> bool: # not efficient - time limit exceed
        stacks = []
        for i in nums:
            if i not in stacks:
                stacks.append(i)
            if i in stacks:
                return True
        return False


    def method_3(self, nums: list[int]) -> bool: # better than 82% memory 94%
        nums = sorted(nums)
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False


    def method_4(self, nums: list[int]) -> bool:
        s = set()
        for j in nums:
            if j in s:
                return True
            s.add(j)
        return False


nums = [1,2,3,1]
# nums = [1,1,1,3,3,4,3,2,4,2]
sol = Solution()
print(sol.containsDuplicate(nums))
print(sol.method_2(nums))
print(sol.method_3(nums))
print(sol.method_4(nums))

