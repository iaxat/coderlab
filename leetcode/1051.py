class Solution:
    def heightChecker(self, heights):

        # method 1
        # count = 0
        # check = sorted(heights)
        # for x,y in zip(heights,check):
        #     if x != y:
        #         count += 1
        # return count

        self.heights = heights
        counter = 0
        len_heights = len(heights)

        for i in range(0,len_heights-1):
            if heights[i] > heights[i+1]:
                heights[i],heights[i+1] = heights[i+1],heights[i]
                counter += 1
            else:
                pass
        print(counter)
        return counter

heights = [5,1,2,3,4]
start = Solution()
start.heightChecker(heights)
