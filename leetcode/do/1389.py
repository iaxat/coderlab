# Easy

class Solution:
    def createTargetArray(self, nums, index):
        result = []
        for i in range(len(index)):
            if len(result)>=i:
                index_point = index[i]
                result.insert(result[index_point],nums[i])
            else:
                result.append(nums[i])
        



nums = [0,1,2,3,4]
index = [0,1,2,2,1]
sol = Solution()
sol.createTargetArray(nums,index)