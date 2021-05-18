# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000


class Solution:
    def romanToInt(self, s):
        result = 0
        s = list(s)
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000
        
        roman_dict = {I:[V,X], X:[L,C], C:[D,M]}
        for i in s:
            

        return result

s = "III"
sol = Solution()
sol.romanToInt(s)