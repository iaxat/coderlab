# Easy

class Solution:
    def removeVowels(self, s: str) -> str:
        # arr = ['a','e','i','o','u']
        # for i in s:
        #     if i in arr:
        #         s = s.replace(i,'')
        # return s


        return ''.join(c for c in s if c not in 'aeiou')



s = 'leetcodeisacommunityforcoders'
sol = Solution()
print(sol.removeVowels(s))
