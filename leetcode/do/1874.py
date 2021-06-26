# Medium

class Solution:
    def minProductSum(self, nums1: list[int], nums2: list[int]) -> int:
        
        # method 1 - time limit exceed
        # results = 0
        # for i in range(len(nums1)):
        #     a = max(nums1)
        #     b = min(nums2)
        #     results += a * b
        #     nums1.pop(nums1.index(a))
        #     nums2.pop(nums2.index(b))
        # return results


        # method 2 - recursion
        results = 0
        if len(nums1) == 0:
            return results
        



nums1 = [5,3,4,2]
nums2 = [4,2,2,5]
sol = Solution()
print(sol.minProductSum(nums1,nums2))
