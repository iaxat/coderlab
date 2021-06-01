# Easy

class Solution:
    def makeGood(self, s: str) -> str:
        stacks = []
        result = 0
        for i in range(len(s)-1):
            s = s.replace(s[i],'')
            print(s)


s = "leEeetcode"
sol = Solution()
sol.makeGood(s)