# Medium
# imp
# functional programming

class Tupl_set():
    def cons(self,a, b):
        # print(a,b)
        def pair(f):
            return f(a, b)
        return pair

    def car(self, pair):
        def f1(v1,v2):
            return v1
        return pair(f1)
    
    def cdr(self, pair):
        def f2(v1,v2):
            return v2
        return pair(f2)

    def sol(self):
        
        return sol.car(self.cons(3,4)), sol.cdr(self.cons(3,4))



sol = Tupl_set()
print(sol.sol())
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
