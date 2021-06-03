# Easy

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j] == target and i<j:
                    result.append(i)
                    result.append(j)
                else:
                    continue

        # return result
        print(result)

        # method 2
        # using the target subtraction
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i<j and target-nums[i]==nums[j]:
                    result = [i,j]
        
        # return result
        print(result)


        # method 3
        # using two pass hash table
        




nums = [2,7,11,15]
target = 9
sol = Solution()
sol.twoSum(nums, target)