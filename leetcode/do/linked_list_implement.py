# Linked List implementation

class Node():
    def __init__(self,data):
        self.next = None
        self.val = data

class Linked_list():
    def __init__(self):
        self.head = None


list1 = Linked_list()
list1.head = Node('Monday')
list2 = Node('Tuesday')
list3 = Node('Wednesday')
list4 = Node('Thursday')
list5 = Node('Friday')
list6 = Node('Saturday')

# linking the node

