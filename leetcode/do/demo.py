# # Linked List implementation

class ListNode():
    def __init__(self,data,next=None):
        self.next = next
        self.val = data

class Linked_list():
    def __init__(self):
        self.head = None

list1 = Linked_list()
list1.head = ListNode('Monday')
list2 = ListNode('Tuesday')
list3 = ListNode('Wednesday')
list4 = ListNode('Thursday')
list5 = ListNode('Friday')
list6 = ListNode('Saturday')

# linking the node
list1.head.next = list2
list2.next = list3
list3.next = list4
list4.next = list5
list5.next = list6

# insert a new node in between list 1 and 2
# create new node
list_middle = ListNode('middle man')

list1.head.next = list_middle
list_middle.next = list2

# while list.next != None:

print(list1.head.next.val)
# ##############################
# prehead = 
