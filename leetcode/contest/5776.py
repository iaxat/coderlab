class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        len_mat = len(mat)
        len_target = len(target)
        temp_matrix = []
        if mat == target:
            return True
        if len_mat == 0 or len_target == 0:
            return False
        if len_mat == 0 and len_target == 0:
            return 0


        



mat = [[0,1],[1,0]]

target = [[1,0],[0,1]]
sol = Solution()
sol.findRotation(mat, target)