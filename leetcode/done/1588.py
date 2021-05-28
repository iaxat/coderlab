# Easy

class Solution:
    def sumOddLengthSubarrays(self, arr):
        counter = 0
        for i in range(len(arr)):
            for j in range(1,len(arr)+1):
                if i != j:
                    temp_arr = arr[i:j]
                    temp_len = len(temp_arr)
                    if temp_len>0:
                        if temp_len%2 != 0:
                            counter+= sum(temp_arr)
                        else:
                            pass

        return counter





arr = [1,4,2,5,3]
sol = Solution()
sol.sumOddLengthSubarrays(arr)