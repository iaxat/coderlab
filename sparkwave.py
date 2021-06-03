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
            new_line.append(line.replace("\n", ""))
        print(new_line)
        return new_line

    # Extract the data from the new_line
    # Which 
    def extract_data(self,new_line):
        print('')


    
    # def create_relation_graph(self):
        

    
    def start_program(self):
        new_line = self.read_file('readme.txt')
        graph_create = self.extract_data(new_line)



sol = Dependent_Libraries()
print(sol.start_program())