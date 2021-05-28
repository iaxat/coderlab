# Easy

class Solution:
    def xorOperation(self, n, start):
        # nums = []
        # xor_data = 0
        # for i in range(n):
        #     pico = start + 2*i
        #     nums.append(pico)
        # for j in range(len(nums)):
        #     if j+1 <= len(nums):
        #         xor_data = xor_data ^ nums[j]
        # return xor_data

        # lst = []
        # while len(lst) != n:
        #     lst.append(str(start))
        #     start += 2
        # return eval("^".join(lst))

        result = start
        for i in range(1, n):
            result ^= start + 2 * i
        return result


n = 5
start = 0
sol = Solution()
print(sol.xorOperation(n,start))