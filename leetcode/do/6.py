# Medium

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)<=1 or numRows == 1:
            return s
        res = ['']*numRows
        index, step = 0, 1
        for c in s:
            res[index] += c
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1
            index += step
        return ''.join(res)





s = "PAYPALISHIRING"
numRows = 3
sol = Solution()
print(sol.convert(s,numRows))
