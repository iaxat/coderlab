# Easy

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:        
        start = end = 0
        time = 0
        for i in word:
            end = keyboard.index(i)
            time += abs(start - end)
            start = end
        
        return time


    # method 2
    def calculateTime2(self, keyboard, word):
        



keyboard = "pqrstuvwxyzabcdefghijklmno"
word = "leetcode"
sol = Solution()
sol.calculateTime(keyboard, word)
