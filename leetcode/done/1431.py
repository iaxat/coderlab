# Easy

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candy = max(candies)
        true_arr = []
        for i in candies:
            if i + extraCandies >= max_candy:
                true_arr.append(True)
            else:
                true_arr.append(False)
        return true_arr



candies = [2,3,5,1,3]
extraCandies = 3
sol = Solution()
sol.kidsWithCandies(candies,extraCandies)