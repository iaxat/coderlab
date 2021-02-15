# Leetcode Weekly Test

class Solution:
    def minOperations(self, s: str) -> int:
        operations = 0
        ar = list(map(lambda x:x, s))
        print(ar)
        for i in len(ar)-1:
            if ar[i] == ar[i+1]:
                operations+=1
                if ar[i+1] == '0':
                    ar[i+1] = '1'
                elif ar[i+1] == '1':
                    ar[i+1] = '0'
            else:
                continue
        return operations

sol = Solution()
sol.minOperations('0000')