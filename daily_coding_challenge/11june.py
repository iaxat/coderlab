# google problem

class Sum_target():
    def calculate(self,nums,target):
        for i in nums:
            a = target - i
            if a in nums:
                return True

nums = [10, 15, 3, 7]
target = 17
sol = Sum_target()
print(sol.calculate(nums,target))
