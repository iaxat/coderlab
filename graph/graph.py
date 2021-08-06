# [a,b],[b,c],[c,d]

class Create():
    def __init__(self, data) -> None:
        self.data = data

    def create_graph_directed(self) -> dict:
        # graph_dict = {}
        # for i in range(0,len(self.data)):
        #     for j in range(1,len(self.data[i])):
        #         key_dict = self.data[i][0]
        #         values_data = self.data[i][j]
        #         if key_dict not in graph_dict.keys():
        #             if values_data is not None:
        #                 graph_dict[key_dict] = [values_data]
        #             else:
        #                 graph_dict[key_dict] = []
        #         else:
        #             if values_data is not None:
        #                 graph_dict[key_dict].append(values_data)
        #             else:
        #                 graph_dict[key_dict] = []
                    
        # return graph_dict

        # 1 for loop
        graph_dict = {}
        for edge in self.data:
            if edge[0] not in graph_dict.keys():
                graph_dict[edge[0]] = [edge[1]]
            else:
                graph_dict[edge[0]].append(edge[1])
            # if edge[1] not in graph_dict.keys():
            #     graph_dict[edge[1]] = []

        return graph_dict


    def create_graph_undirected(self) -> dict:
        graph_dict = {}
        for edge in self.data:
            if edge[0] not in graph_dict.keys():
                graph_dict[edge[0]] = [edge[1]]
            else:
                graph_dict[edge[0]].append(edge[1])
            if edge[1] not in graph_dict.keys():
                graph_dict[edge[1]] = [edge[0]]
            else:
                graph_dict[edge[1]].append(edge[0])
        return graph_dict


    def dfs_graph_directed(self):
        graph_dict_data = self.create_graph_directed()
        # stack = ['a']
        stack = []
        for node in graph_dict_data:
            stack.append(node)
        visited = set()
        while stack:
            current = stack.pop()
            if current not in visited:
                for child in graph_dict_data[current]:
                    if child not in visited:
                        stack.append(child)
                visited.add(current)
        print(visited)


    def dfs_recursion(self):
        





data = [['a','b'],['a','c'],['c','d']]
sol = Create(data)
print(sol.create_graph_directed())
# print(sol.create_graph_undirected())
# sol.dfs_graph_directed()
# {a=[b, c], b=[a], c=[a, d], d=[c]}

# detect cycle in graph
# recursion
# shortest distance
