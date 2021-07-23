# Easy

class Solution():
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        counter = []
        for counts in range(1,n+1):
            counter.append(counts)

        while len(counter) > 1:
            for nums in trust:
                i, j = nums
                if i in counter:
                    counter.remove(i)
        if len(counter)==1:
            return counter[0]
        else:
            return -1


n = 3
trust = [[1,2],[2,3]]
sol = Solution()
print(sol.findJudge(n,trust))
