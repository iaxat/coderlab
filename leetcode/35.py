class Solution:
    def relativeSortArray(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2
        result = []
        extra = []
        for i in arr2:
            for j in arr1:
                if i == j:
                    result.append(j)
                    
                if j not in arr2:
                    extra.append(j)

        extra = list(set(extra))
        extra.sort(reverse=False)
        print(extra)
        for k in extra:
            result.append(k)
        # print(result)
        return result

arr1 = [2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31]
arr2 = [2,42,38,0,43,21]
sol = Solution()
sol.relativeSortArray(arr1,arr2)
