# Easy

class Solution:
    def removeDuplicates(self, S: str) -> str:
        output = []

        for ch in S:
            if output and ch == output[-1]: 
                output.pop()
            else: 
                output.append(ch)
        return ''.join(output)

S = "abbaca"
sol = Solution()
print(sol.removeDuplicates(S))