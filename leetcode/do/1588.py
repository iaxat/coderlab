# Easy

class Solution:
    def sumOddLengthSubarrays(self, arr):
        counter = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                temp_arr = arr[i:j]
                temp_len = len(temp_arr)
                if temp_len%2 != 0:
                    counter+= sum(temp_arr)

        print(counter)





arr = [1,4,2,5,3]
sol = Solution()
sol.sumOddLengthSubarrays(arr)