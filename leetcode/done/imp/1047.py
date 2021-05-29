# Easy

class Solution:
    def removeDuplicates(self, S: str) -> str:
        result = []

        for i in S:
            if result and i == result[-1]: 
                result.pop()
            else: 
                result.append(i)
        return ''.join(result)

S = "abbaca"
sol = Solution()
print(sol.removeDuplicates(S))