# Easy

class Solution:
    def shuffle(self, nums, n):
        len_nums = int(len(nums))
        half = int(len_nums/2)
        result = []
        # one_arr = nums[0:half]
        # two_arr = nums[half:len_nums]
        # for i in range(len(one_arr)):
        #     result.append(one_arr[i])
        #     result.append(two_arr[i])
        # print(result)

        
        
        # method 2
        for i in range(half):
            diff = half
            result.append(nums[i])
            result.append(nums[i+half])
        # print(result)

        return result


        # method 3
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i+n])
        # print(result)


nums = [2,5,1,3,4,7]
n = 3
sol = Solution()
sol.shuffle(nums, n)