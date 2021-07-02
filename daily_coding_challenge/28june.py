# Hard

class Solution():
    def __init__(self, k, arr_) -> None:
        self.k = k
        self.arr_ = arr_
        self.results = []
    
    def do_it(self):
        # using the sliding window approach
        for i in range(len(self.arr_)):
            if i+self.k <= len(self.arr_):
                self.results.append(max(self.arr_[i:i+self.k]))
        return self.results
        

        # using the recursion approach
    # def do_it_recursion(self,arr_):
        

        
        
        # using the loop approach
    # def do_it_loop(self):




k = 3
arr_ = [10, 5, 2, 7, 8, 7]
sol = Solution(k, arr_)
print(sol.do_it())
# print(sol.do_it_recursion())
# print(sol.do_it_loop())
