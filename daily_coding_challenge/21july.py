# Medium

class Route_Finder():
    def __init__(self, path, start_point) -> None:
        self.path = path
        self.start_point = start_point

    # def final_route(self):
    #     result = []
    #     path_dict = {}
    #     for edge in self.path:
    #         if edge[0] not in path_dict.keys():
    #             path_dict[edge[0]] = [edge[1]]
    #         else:
    #             path_dict[edge[0]].append(edge[1])
    #     print(path_dict)




path = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
#  ['A', 'B', 'C', 'A', 'C']
# ['A', 'C', 'A', 'B', 'C']
start_point = 'A'
sol = Route_Finder(path, start_point)
print(sol.final_route())
