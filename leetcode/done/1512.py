# Easy
import collections
class Solution:
    def numIdenticalPairs(self, nums):
        # pairs = 0
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j and i<j:
        #             if nums[i] == nums[j]:
        #                 pairs+=1
        
        # print(pairs)
        # return pairs

        print(sum(k * (k - 1) / 2 for k in collections.Counter(nums).values()))

nums = [1,2,3,1,1,3]
sol = Solution()
sol.numIdenticalPairs(nums)