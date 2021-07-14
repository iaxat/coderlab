# Create linked list from the array
# used to be imported to another file
# 
class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create_linkedList(self, data):
        list_head = ListNode()
        prev = list_head
        for i in data:
            a = ListNode(i)
            prev.next=a
            prev = prev.next
        return list_head.next

create = ListNode()
create.create_linkedList()
