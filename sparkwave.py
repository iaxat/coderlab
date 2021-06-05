# Job Application Coding Assignment

# Funtions implemented in the file
class Dependent_Libraries:
    def __init__(self) -> None:
        self.data_dict = {}

    def read_file(self, file):
        with open(file) as f:
            lines = f.readlines()
        new_line = []
        for line in lines:
            temp_line = (
                line.replace(" depends on ", ",").replace(" ", "").replace("\n", "")
            )
            new_line.append(temp_line)
        return new_line

    # Extract the data from the new_line
    # Which will return the values
    def extract_data(self, new_line):
        total_elements = []
        for i in range(len(new_line)):
            if len(new_line[i]) >= 4:
                chunk = new_line[i].split(",")
                part = list(chunk[1])
                if chunk[0] in self.data_dict.keys():
                    self.data_dict[chunk[0]].append(part)
                else:
                    self.data_dict[chunk[0]] = part
                total_elements.append(chunk[0])
                for k in chunk[1]:
                    total_elements.append(k)
            elif len(new_line[i]) < 4:
                chunk = new_line[i].split(",")
                if chunk[0] in self.data_dict.keys():
                    self.data_dict[chunk[0]].append(chunk[1])
                else:
                    self.data_dict[chunk[0]] = list(chunk[1])
                total_elements.append(chunk[1])

        for ele in total_elements:
            if ele not in self.data_dict.keys():
                self.data_dict[ele] = []

        return self.data_dict

    # creating graph and using it to find relation
    # BFS model
    def create_relation_graph(self, data_dict, node):
        visited = []
        queue = []
        result = []
        # temp array for logic implementation
        # conditions for specific snearios
        if len(data_dict[node]) == 0 and len(queue) > 0:
            return queue
        elif len(data_dict[node]) == 0 and len(queue) == 0:
            return ""
        visited.append(node)
        queue.append(node)
        while queue:
            m = queue.pop(0)
            result.append(m)
            for neighbour in data_dict[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

        str_final = result[0] + ' depends on ' + ''.join(result[1:len(result)])
        print(str_final)
        return str_final

    # running program
    def start_program(self):
        new_line = self.read_file("readme.txt")
        data_dict = self.extract_data(new_line)
        for data in data_dict.keys():
            self.create_relation_graph(data_dict, data)


# initiation
sol = Dependent_Libraries()
sol.start_program()
