# Easy

class Solution:
    def maximumWealth(self, accounts):
        # result = []
        # for i in accounts:
        #     result.append(sum(i))
        # max_res = max(result)

        return max(map(sum, accounts))


accounts = [[1,2,3],[3,2,1]]
sol = Solution()
sol.maximumWealth(accounts)