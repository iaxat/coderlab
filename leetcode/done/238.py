# 

import numpy as np

class Solution:
    # method 1
    def productExceptSelf(self, nums):
        nums = np.array(nums)
        result = []
        for i in range(0,len(nums)):
            new_a = np.delete(nums, i)
            final = np.prod(new_a)
            if abs(final) <= 0xffffffff:
                result.append(final)
        print(result)
        return result

nums = [1,2,3,4]
sol = Solution()
sol.productExceptSelf(nums)