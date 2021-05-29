# Easy

class Solution:
    def removeDuplicates(self, s: str) -> str:
        a = True
        s = list(s)
        while a == True:
            for i in range(len(s)):
                if i+1 <= len(s)-1:
                    if s[i] == s[i+1]:
                        print(s[i],s[i+1])
                        s.pop(i)
                        s.pop(i)
                        print(s)
                        i = 0
            
                else:
                    a = False
        s = str(s)
        print(s)
        return s

s = "abbaca"
sol = Solution()
sol.removeDuplicates(s)