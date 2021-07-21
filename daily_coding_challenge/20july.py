# Hard

from collections import Counter

class Google_duplicate():
    def __init__(self, data) -> None:
        self.data = data

    def unique_find(self):
        result = Counter(self.data)
        for i in result:
            if result[i] == 1:
                return i


    # method 2
    def method_2(self):
        result = {}
        for i in self.data:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
        for i in result:
            if result[i] == 1:
                print(i)
                return i

    
    # method 3
    def method_3(self, data):
        





data = [6, 1, 3, 3, 3, 6, 6]
sol = Google_duplicate(data)
sol.unique_find()
sol.method_2()
sol.method_3(data)
