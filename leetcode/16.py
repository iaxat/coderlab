class Solution:
    def threeSumClosest(self, nums, target):
        self.nums = nums
        self.target = target
        results = []
        nums = sorted(nums)
        for i in nums:
            for j in nums:
                for k in nums:
                    if nums.index(i)!=nums.index(j)!=nums.index(k):
                        count = i+j+k
                        results.append(count)

        for l in results:
            if l<0:
                
            if l>0:


nums = [-1,2,1,-4]
target = 1
sol = Solution()
sol.threeSumClosest(nums, target)