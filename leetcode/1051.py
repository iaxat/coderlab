# Students are asked to stand in non-decreasing order of heights for an annual photo.
# Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.
# Notice that when a group of students is selected they can reorder in any possible way between themselves and the non selected students remain on their seats.

# Input: heights = [1,1,4,2,1,3]    Output: 3
# Input: heights = [5,1,2,3,4]  Output: 5

class Solution:
    def heightChecker(self, heights):
        # method 1
        # count = 0
        # check = sorted(heights)
        # for x,y in zip(heights,check):
        #     if x != y:
        #         count += 1
        # return count

        # method 2
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
