# Easy

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_1 = max(len(x) for x in s.split('0'))
        max_0 = max(len(x) for x in s.split('1'))
        return max_1>max_0

s = "1101"
sol = Solution()
print(sol.checkZeroOnes(s))