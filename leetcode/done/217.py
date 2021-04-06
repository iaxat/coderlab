from collections import Counter
class Solution:
    def containsDuplicate(self, nums):
        self.nums = nums

        # # Method 1
        # a = Counter(nums)
        # for k in a:
        #     print(a[k])
        #     if a[k]>=2:
        #         return True
        # else:
        #     return False

        # Method 2
        nums = sorted(nums)
        for i in range(0,len(nums)):
            if nums[i] == nums[i+1] and i+1<=len(nums):
                return True
        else:
            return False

nums = [2,14,18,22,22]
sol = Solution()
sol.containsDuplicate(nums)