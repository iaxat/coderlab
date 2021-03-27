from collections import Counter

class Solution:
    def largeGroupPositions(self, s):
        self.s = s
        result = []
        s = list(s)
        counter = Counter(s)
        for key in counter:
            if counter[key] >=3:
                result.append(key)
        if len(result) == 0:
            return []
        else:
            for i in result:
                final_result = []
                for j in range(0,len(s)):
                    if i == s[j]:
                        final_result.append(int(j))
                output_ = [[final_result[0],final_result[len(final_result)-1]]]


        print(output_)

s = "abbxxxxzzy"
sol = Solution()
sol.largeGroupPositions(s)