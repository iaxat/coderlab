import unittest

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
            line = line.replace(" depends on ",",")
            temp_line = line.replace(" ","")
            new_line.append(temp_line.replace("\n", ""))
        return new_line


    # Extract the data from the new_line
    # Which will return the values
    def extract_data(self,new_line):
        self.data_dict = data_dict = {}
        for i in range(len(new_line)):
            if len(new_line[i])>=4:
                chunk = new_line[i].split(',')
                for j in range(len(chunk)):
                    part=list(chunk[1])
                    data_dict[chunk[0]] = part
            elif len(new_line[i])<4:
                chunk = new_line[i].split(',')
                data_dict[chunk[0]] = list(chunk[1])
        print(data_dict)
        return data_dict


    def create_relation_graph(self,data_dict,node):
        visited = [] # List for visited nodes.
        queue = [] # Initialize a queue
        if data_dict[node] == []:
            return queue
        visited.append(node)
        queue.append(node)
        while queue:# Creating loop to visit each node
            m = queue.pop(0) 
            print (m, end = " ") 
            for neighbour in data_dict[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return queue


    def start_program(self):
        new_line = self.read_file('readme.txt')
        data_dict = self.extract_data(new_line)
        graph = {'X': ['Y', 'R'], 'Y': ['Z'], 'R':[], 'Z':[]}
        result = self.create_relation_graph(graph,"Z")
        print(result)

# initiation
sol = Dependent_Libraries()
sol.start_program()