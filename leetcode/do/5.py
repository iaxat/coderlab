# Medium

class Solution:
    def longestPalindrome(self, s: str) -> str:

        # method 1  - time exceeded
        # result = []
        # final = 0
        # for i in range(0,len(s)):
        #     for j in range(1,len(s)+1):
        #         data = s[i:j]
        #         if data == data[::-1] and data != '':
        #             result.append((data))
        # for k in result:
        #     if final < len(k):
        #         final = len(k)
        #         res = k
        # return res


        # method 2
        


s = "babad"
sol = Solution()
print(sol.longestPalindrome(s))