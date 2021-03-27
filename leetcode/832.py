class Solution:
    def flipAndInvertImage(self, image):
        self.image = image
        
        
        
        for i in range(0,len(image)):
            for j in range(0,len(image[i])):
                # reverse matrix
                image[i] = image[i][::-1]
                
                if image[i][j] == 0:
                    image[i][j] = 1
                    
                elif image[i][j] == 1:
                    image[i][j] = 0
        print(image)
        return image
        print(image)

image = [[1,1,0],[1,0,1],[0,0,0]]
sol = Solution()
sol.flipAndInvertImage(image)
