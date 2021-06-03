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


        return data_dict


    def create_relation_graph(self):
        print('')

    
    def start_program(self):
        new_line = self.read_file('readme.txt')
        data_dict = self.extract_data(new_line)
        # print(result) = self.create_relation_graph(data_dict)



# initiate
sol = Dependent_Libraries()
print(sol.start_program())