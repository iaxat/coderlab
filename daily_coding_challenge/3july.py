# Easy

class Solution():
    def __init__(self,arr_):
        self.arr_ = arr_
        self.start = arr_[-1][0]
        self.end = arr_[0][0]
        self.results = []

    def find(self):
        if self.start == 't':
            return
        for i in self.arr_:
            for j in i:
                

        return self.results
        
        


arr_ = [['f', 'f', 'f', 'f'],['t', 't', 'f', 't'],['f', 'f', 'f', 'f'],['f', 'f', 'f', 'f']]
sol = Solution(arr_)
print(sol.find())
