# Easy

class Solution:
    def missingNumber(self, nums: list[int]) -> int: # method 1
        nums = sorted(nums)
        for i in range(0,len(nums)):
            if nums[i] == i:
                continue
            else:
                return i
        return len(nums)



    def method_2(self,nums): # method 2 using set method
        number_set = set(nums)
        n_range = len(nums) + 1
        for i in range(n_range):
            if i not in number_set:
                return i

    
    def method_3(self, nums): # method 3 using bit manipulation
        





nums = [3,0,1]
sol = Solution()
# print(sol.missingNumber(nums))
print(sol.method_2(nums))
print(sol.method_3(nums))
