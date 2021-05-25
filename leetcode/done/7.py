# 

class Solution:
    def reverse(self, x):
        if x>=(-2**31) and (x<=2**31-1):
            if int(x)<0:
                x = (int(x))*-1
                x = str(x)
                x = x[::-1]
                x = (int(x))*-1
            else:
                x = str(x)
                x = x[::-1]
                x = int(x)
            if x>=(-2**31) and (x<=2**31-1):
                return x
            else:
                x = 0
        else:
            x = 0
        
        return x


x = 1534236469
sol = Solution()
sol.reverse(x)