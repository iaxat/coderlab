# Easy

from typing import Counter


class Solution:
    def decompressRLElist(self, nums):
        counter = 0
        n = len(nums)
        ans = []
        while counter < n:
            temp = [nums[counter+1]] * nums[counter]
            counter += 2
            ans += temp
        return ans
        # return sum((a * [b] for a, b in zip(*[iter(nums)]*2)), [])
        # return [b for a, b in zip(*[iter(nums)]*2) for _ in range(a)]

nums = [1,2,3,4]
sol = Solution()
sol.decompressRLElist(nums)