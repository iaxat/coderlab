# Medium

class Solution():
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        graph_dict = {}
        for i in graph:
            graph_dict[i] = graph[i]
                



graph = [[1,2],[3],[3],[]]
sol = Solution()
sol.allPathsSourceTarget(graph)
