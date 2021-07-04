class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        counter = 0

        if 0 in dist:
            return counter

        min_data = min(dist)
        min_data_index = dist.index(min_data)
        dist[min_data_index] = -1
        # monster killed
        counter += 1
        print(dist)
        for i in range(0,len(dist)):
            if dist[i] != -1:
                dist[i] = dist[i] - speed[i]
        self.eliminateMaximum(dist,speed)

        return counter
                



dist = [1,3,4]
speed = [1,1,1]
sol = Solution()
print(sol.eliminateMaximum(dist, speed))

