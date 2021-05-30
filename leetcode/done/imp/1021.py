# Easy

class Solution:
    def removeOuterParentheses(self, s):
        stacks = []
        result = ''
        for ch in s:
            stacks.append(ch)
            if (stacks.count('(') == stacks.count(')')):
                result += (''.join(stacks[1:-1]))
                stacks.clear()
    
        return (result)




s = "(()())(())"
sol = Solution()
print(sol.removeOuterParentheses(s))