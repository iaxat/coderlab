# Job Application Coding Assignment

# Funtions implemented in the file
class Dependent_Libraries():
    def __init__(self) -> None:
        pass


    def read_file(self,file):
        with open(file) as f:
            lines = f.readlines()
        new_line = []
        for line in lines:
            temp_line = line.replace(" depends on ",",")
            new_line.append(temp_line.replace("\n", ""))
        return new_line


    # Extract the data from the new_line
    # Which will return the values
    def extract_data(self,new_line):
        self.data_dict = data_dict = {}
        for i in range(len(new_line)):
            
            # if i[0] in data_dict.keys():
            #     data_dict[i[0]].append()
            # else:
            #     data_dict[i[]]

            print(new_line[i])
        print(data_dict)
        return data_dict


    def create_relation_graph(self,graph,node):
        visited = [] # List for visited nodes.
        queue = [] # Initialize a queue
        visited.append(node)
        queue.append(node)
        while queue:# Creating loop to visit each node
            m = queue.pop(0) 
            print (m, end = " ") 
            for neighbour in graph[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return queue


    def start_program(self):
        new_line = self.read_file('readme.txt')
        data_dict = self.extract_data(new_line)
        for i in range(len(data_dict)):
            result = self.create_relation_graph(data_dict,data_dict[i])
            print(result)


# initiation
sol = Dependent_Libraries()
print(sol.start_program())