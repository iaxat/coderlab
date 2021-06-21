# Medium

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stacks = []
        results = 0
        if len(s) > 0:
            for i in range(len(s)):
                for j in range(i,len(s)):
                    if s[j] not in stacks:
                        stacks.append(s[j])
                        print(stacks)
                    else:
                        if results < len(stacks):
                            results = len(stacks)
                        stacks.clear()

        return results


s = "jbpnbwwd"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))
