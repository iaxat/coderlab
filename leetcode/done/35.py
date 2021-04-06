from collections import Counter

class Solution:
    def relativeSortArray(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2
        result = []
        extra = []
        dict_ = {}

        arr1.sort(reverse=False)
        dict_ = Counter(arr1)

        for i in arr2:
            for j in arr1:
                if i == j:
                    result.append(j)

                if j not in arr2:
                    extra.append(j)

        extra = list(set(extra))
        extra.sort(reverse=False)
        # print(extra)

        for key in extra:
            if key in dict_:
                value_ = dict_[key]
                value_ = int(value_)
                if value_ == 1:
                    result.append(key)
                elif value_>1:
                    for z in range(value_):
                        result.append(key)

        print(result)
        return result

arr1 = [0,1,2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

sol = Solution()
sol.relativeSortArray(arr1,arr2)
