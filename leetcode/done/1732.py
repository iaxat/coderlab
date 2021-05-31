# Easy

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        gain.insert(0,0)
        result = []
        data = 0
        for i in range(len(gain)):
            data += gain[i]
            result.append(data)
        return max(result)

gain = [-5,1,5,0,-7]
sol = Solution()
print(sol.largestAltitude(gain))