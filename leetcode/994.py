# Medium
from random import randint

class Solution():

    # function to assign value
    def gen_random_value(self):
        return randint(0,50)

    def orangesRotting(self, grid: list[list[int]]) -> int:
        graph_structure = []
        graph_dict = {}
        stacks = []
        
        # random value assign
        for i in grid:
            for j in range(len(i)):
                random_value = self.gen_random_value()

                while random_value in stacks and True:
                    random_value = self.gen_random_value()
                    if random_value not in stacks:
                        False

                i[j] = random_value
                stacks.append(random_value)

        # edge connecting
        for i in range(0,len(grid)-1):
            out_one, out_two = grid[i], grid[i+1]

            for j in range(0,len(grid)-1):

                # same column
                if out_one[j] and out_two[j] or out_one[j] == 0 or out_two[j] == 0:
                    column_data = [in_one_col, in_two_col] = out_one[j], out_two[j]
                    
                    graph_structure.append(list(column_data))

                # same diagonal
                if out_one[j] and out_two[j+1] or out_one[j] == 0 or out_two[j+1] == 0:
                    diagonal_data = [in_one_diag, in_two_diag] = out_one[j], out_two[j+1] 

                    graph_structure.append(list(diagonal_data))

                # same row
                if out_one[j] and out_one[j+1] or out_one[j] == 0 or out_one[j+1] == 0:
                    row_data = [in_one_row, in_two_row] = out_one[j], out_one[j+1]

                    graph_structure.append(list(row_data))

        # create graph
        for edge in graph_structure:
            if edge[0] not in graph_dict.keys():
                graph_dict[edge[0]] = [edge[1]]
            else:
                graph_dict[edge[0]].append(edge[1])






        print(graph_structure)
        print(graph_dict)

grid = [[2,1,1],[1,1,0],[0,1,1]]
sol = Solution()
sol.orangesRotting(grid)
