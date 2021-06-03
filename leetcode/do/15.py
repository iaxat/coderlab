# Medium

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        counter = 0
        if len(nums) <= 1:
            return result
        while len(result)<2:
            