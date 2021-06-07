# Medium

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = []
        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(len_nums):
                for k in range(len_nums):
                    if i != j and i != k and j!=k:
                        if nums[i] + nums[j] + nums[k] == 0:
                            if i < j and j < k:
                                data = [nums[i], nums[j], nums[k]]
                                if data not in results:
                                    results.append(data)
        print(results)

nums = [-1,0,1,2,-1,-4]
sol = Solution()
sol.threeSum(nums)