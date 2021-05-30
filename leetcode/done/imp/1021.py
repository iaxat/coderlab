# Easy

class Solution:
    def removeOuterParentheses(self, s):
        # method 1
        stacks = []
        result = ''
        for ch in s:
            stacks.append(ch)
            if (stacks.count('(') == stacks.count(')')):
                result += (''.join(stacks[1:-1]))
                stacks.clear()
        return (result)


        # method 2 stack


s = "(()())(())"
sol = Solution()
print(sol.removeOuterParentheses(s))