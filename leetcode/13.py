class Solution:
    def romanToInt(self, s):
        roman_dict={'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000}
        result=0
        x=0
        for i in s[::-1]:
            if x<=roman_dict[i]:
                sum+=roman_dict[i]
                x=roman_dict[i]
            else:
                sum-=roman_dict[i]
        return result

s = "IXCX"
sol = Solution()
sol.romanToInt(s)