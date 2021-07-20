# [a,b],[b,c],[c,d]

from typing import get_args


class Create():
    def __init__(self, data) -> None:
        self.data = data

    def create_graph_directed(self) -> dict:
        graph_dict = {}
        for i in range(0,len(self.data)):
            for j in range(1,len(self.data[i])):
                key_dict = self.data[i][0]
                values_data = self.data[i][j]
                if key_dict not in graph_dict.keys():
                    graph_dict[key_dict] = [values_data]
                else:
                    graph_dict[key_dict].append(values_data)
        return graph_dict


    def create_graph_undirected(self) -> dict:
        graph_dict = {}
        for edge in self.data:
            print(edge[0])
            if edge[0] not in graph_dict.keys():
                graph_dict[edge[0]] = []
            else:
                graph_dict[edge[0]] = edge[1]
        return graph_dict

        # for i in range(0,len(self.data)):
        #     a = 0
        #     key_dict = self.data[i][a]
        #     for j in range(0,len(self.data[i])):
        #         values_data = self.data[i][j]
        #         if key_dict not in graph_dict.keys() and key_dict != values_data:
        #             graph_dict[key_dict] = [values_data]
        #         elif key_dict in graph_dict.keys() and key_dict != values_data:
        #             graph_dict[key_dict].append(values_data)
        #     a += 1

        return graph_dict


data = [['a','b'],['a','c'],['c','d']]
sol = Create(data)
# print(sol.create_graph_directed())
print(sol.create_graph_undirected())
# {a=[b, c], b=[a], c=[a, d], d=[c]}
