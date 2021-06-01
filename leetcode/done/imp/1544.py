# Easy

class Solution:
    def makeGood(self, s: str) -> str:
        stacks = []
        diff = abs(ord('c') - ord('C'))
        for c in s:
            if not stacks:
                stacks.append(c)
            else:
                if abs(ord(stacks[-1]) - ord(c)) == diff:
                    stacks.pop()
                else:
                    stacks.append(c)
        return ''.join(stacks)

s = "leEeetcode"
sol = Solution()
print(sol.makeGood(s))