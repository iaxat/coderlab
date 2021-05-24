# Medium

class Solution:
    def merge(self, intervals):
        temp_arr = []
        for i in intervals:
            for j in range(0,2):
                temp_arr.append(i[j])
        print(temp_arr)
        temp_arr = sorted(temp_arr)
        print(temp_arr)


    
intervals = [[1,3],[2,6],[8,10],[15,18]]
sol = Solution()
sol.merge(intervals)