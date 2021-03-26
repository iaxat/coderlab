class Solution:
    def maxProfit(self, prices):
        buy = 0
        sell = 0
        profit = []

        le = len(prices)
        for i in range(le):
            for j in range(le):
                if i != j:
                    if (prices[i]<prices[j]) and (prices[j]-prices[i]>=0):
                        buy = prices[i]
                        sell = prices[j]
                        print(buy)
                        diff = buy-sell
                        # print(diff)
                        profit.append(diff)




        # print(profit)
        return profit

prices = [2,4,1]
sol = Solution()
sol.maxProfit(prices)
