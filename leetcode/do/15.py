# Medium

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        # method 1

        results = {}
        temp_arr = []
        len_nums = len(nums)
        for i in range(len_nums):
            j = i+1
            for j in range(len_nums):
                k = j+1
                for k in range(len_nums):
                    if i != j and i != k and j!=k:
                        if nums[i] + nums[j] + nums[k] == 0:
                            if i < j and j < k and i<k:
                                data = {nums[i], nums[j], nums[k]}
                                if data not in results:
                                    results.append(data)
        print(results)


        # method 2
        stacks = []
        hash_map = {}
        for i in range(len(nums)):
            






nums = [-1,0,1,2,-1,-4]
sol = Solution()
sol.threeSum(nums)