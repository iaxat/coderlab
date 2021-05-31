# Easy

class Solution:
    def createTargetArray(self, nums, index):
        target_arr = []
        for i in range(len(index)):
            target_arr.insert(index[i],nums[i])
        # return target_arr

        # method 2 without using insert
        lst = []
        for i in range(len(nums)):
            lst = lst[:index[i]] + [nums[i]] + lst[index[i]:]
            print(lst)
        print(lst)

        lst = []
        for i in range(len(nums)):
            lst[index[i]:index[i]] = [nums[i]]
        print(lst)





nums = [0,1,2,3,4]
index = [0,1,2,2,1]
sol = Solution()
sol.createTargetArray(nums,index)