# Easy

from typing import DefaultDict


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
        total = 0
        prev = 0
        myDict = DefaultDict()
        for idx, char in enumerate(keyboard):
            myDict[char] = idx
        for i in word:
            total = total + abs(myDict[i] - prev)
            prev = myDict[i]
        return total



keyboard = "pqrstuvwxyzabcdefghijklmno"
word = "leetcode"
sol = Solution()
sol.calculateTime(keyboard, word)
sol.calculateTime2(keyboard, word)
