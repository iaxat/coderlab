# Easy

class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        len_arr = len(arr)
        result = []
        for i in range(len_arr):
            if i >= 0:
                for j in range(len_arr):
                    if i<j:
                        for k in range(len_arr):
                            if j<k:
                                if k<len_arr:
                                    if arr[i] - arr[j] <= a and arr[j] - arr[k] <= b and arr[i] - arr[k] <= c:
                                        res_temp = arr[i],arr[j],arr[k]
                                        res_temp = tuple(res_temp)
                                        if res_temp not in result:
                                            result.append(res_temp)
                                            result_len = len(result)
        print(result)


arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
sol = Solution()
sol.countGoodTriplets(arr,a,b,c)