# Medium

class Solution():
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        
        # 0 create graph
        dict_graph = {}
        for i in range(0,len(graph)):
            dict_graph[i] = graph[i]
        
        # 1 fill stack
        stacks = []
        visited = set()
        for i in dict_graph.keys():
            current = i
            if current not in visited:
                visited.add(current)
                stacks.append(current)
                for j in dict_graph[i]:
                    current = j
                    if current not in visited:
                        visited.add(current)
                        stacks.append(current)
        print(visited)
        print(current)



graph = [[1,2],[3],[3],[]]
sol = Solution()
print(sol.allPathsSourceTarget(graph))
