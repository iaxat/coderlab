# Easy

class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        i, j = edges[0]
        k = edges[1]
        
        # if i == k or i == l:
        #     return i
        # if j == k or j == l:
        #     return j
        if i in k:
            return i
        if j in k:
            return j




edges = [[1,2],[2,3],[4,2]]
sol = Solution()
print(sol.findCenter(edges))
