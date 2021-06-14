# Hard


class Solution():
    def analysis(self,nums):
        results = []
        nums = sorted(nums,reverse=True)
        print(nums)
        for i in range(len(nums)-1):
            if nums[i] > 0 and nums[i+1]>0:
                # case 1
                if nums[i] - nums[i+1] > 1:
                    results.append(nums[i+1]+1)

        # case 2
        if len(results) == 0:
            if nums[0]>0:
                results.append(nums[0]+1)

        return min(results)


nums = [1, 2, 0]
# [1, 2, 0]
sol = Solution()
print(sol.analysis(nums))
