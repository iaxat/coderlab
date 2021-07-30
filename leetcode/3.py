# Medium

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        sliding_window = []
        counter = 0
        for i in range(0,len(s)):
            for j in range(i+1,len(s)):
                sliding_window = s[i:j]
                if len(set(sliding_window)) == len(sliding_window):
                    
                    if len(sliding_window) > counter:
                        counter = len(sliding_window)
        print(counter)


s = "dvdf"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))
