# Medium

class Route_Finder():
    def __init__(self, path, start_point) -> None:
        self.path = path
        self.start_point = start_point

    def final_route(self):
        print('')
        




path = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
#  ['A', 'B', 'C', 'A', 'C']
# ['A', 'C', 'A', 'B', 'C']
start_point = 'A'
sol = Route_Finder(path, start_point)
print(sol.final_route())
