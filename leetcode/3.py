# Medium

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stacks = []
        counter = 0
        for i in range(len(s)):
            
            while s[i] not in stacks:
                stacks.append(s[i])
            

        return len(stacks)

s = "pwwkew"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))
