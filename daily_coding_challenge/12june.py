# Uber
from functools import partial
import numpy as np
from numpy.core.defchararray import multiply

class Solution():
    def mult_find(self,arr_):
        self.arr_ = arr_
        results = []
        for i in range(len(arr_)):
            sub_arr = np.delete(arr_,i)
            re = np.prod(sub_arr)
            # print(re)
            # results.append(re)

    def mult_nonp(self,arr_):
        results = []
        for i in arr_:
            temp_arr = arr_.copy()
            counter = 1
            temp_arr.remove(i)
            for j in temp_arr:
                counter *= j
            results.append(counter)

        print(results)


            


arr_ = [1, 2, 3, 4, 5]
sol = Solution()
sol.mult_nonp(arr_)
