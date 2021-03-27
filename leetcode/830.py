from collections import Counter
import re

class Solution:
    def largeGroupPositions(self, s):
        self.s = s
        # result = []
        # output_ = []
        # s = list(s)
        # counter = Counter(s)
        
        # for key in counter:
        #     if counter[key] >=3:
        #         result.append(key)
        # # s = str(s)
        # # for o in result:
        # #     res = max(re.findall('((?:' + re.escape(o) + ')*)', s),key = len)
        # # print(result)
        
        # if len(result) == 0:
        #     return []
        # else:
        #     for i in result:
        #         final_result = []
        #         for j in range(0,len(s)):
        #             if i == s[j]:
        #                 final_result.append(int(j))
        #         output_.append([final_result[0],final_result[len(final_result)-1]])
        if len(s)<3:
            return []






        

s = "abcdddeeeeaabbbcd"
print('[[3,5],[6,9],[12,14]]')
sol = Solution()
sol.largeGroupPositions(s)