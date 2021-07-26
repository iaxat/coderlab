# Medium

class Solution():
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        graph_dict = {}
        for i in range(0,len(graph)):
            graph_dict[i] = graph[i]
        print(graph_dict)
        results = []
        stacks = [0]
        while stacks:
            temp_res = []
            for i in graph_dict.keys():
                

graph = [[1,2],[3],[3],[]]
sol = Solution()
sol.allPathsSourceTarget(graph)
