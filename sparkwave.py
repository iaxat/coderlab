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
        total_elements = []
        self.data_dict = data_dict = {}
        for i in range(len(new_line)):

            if len(new_line[i])>=4:
                chunk = new_line[i].split(',')
                for j in range(len(chunk)):
                    part=list(chunk[1])
                    data_dict[chunk[0]] = part
                total_elements.append(chunk[0])
                for k in chunk[1]:
                    total_elements.append(k)

            elif len(new_line[i])<4:
                chunk = new_line[i].split(',')
                data_dict[chunk[0]] = list(chunk[1])
                total_elements.append(chunk[1])
        
        for ele in total_elements:
            if ele not in data_dict.keys():
                data_dict[ele] = []
            

        print(data_dict)
        return data_dict


    def create_relation_graph(self,data_dict,node):
        visited = []
        queue = []

        if data_dict[node] == [] and len(queue)>0:
            return queue

        elif data_dict[node] == [] and len(queue)==0:
            return ''

        visited.append(node)
        queue.append(node)

        while queue:
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
        # graph = {'X': ['Y', 'R'], 'Y': ['Z'], 'R':[], 'Z':[]}
        result = self.create_relation_graph(data_dict,"X")
        print(result)

# initiation
sol = Dependent_Libraries()
sol.start_program()