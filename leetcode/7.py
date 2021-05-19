



class Solution:
    def reverse(self, x):
        x = str(x)
        if int(x)<0:
            x = (int(x))*-1
            x = str(x)
            x = x[::-1]
            x = (int(x))*-1
        else:
            x = x[::-1]

        print(x)


x = -123
sol = Solution()
sol.reverse(x)