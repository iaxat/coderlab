# Medium
# from create_linkedLIst import ListNode

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = []
        b = []
        while l1 and l2:
            a.append(l1.val)
            l1 = l1.next

            b.append(l2.val)
            l2 = l2.next
        
        

        print(a, ' ', b)
    

l1 = [2,4,3,5]
l2 = [5,6,4]

def create_linkedList(data):
    list_head = ListNode()
    prev = list_head
    for i in data:
        a = ListNode(i)
        prev.next=a
        prev = prev.next
    return list_head.next

sol = Solution()
sol.addTwoNumbers(create_linkedList(l1), create_linkedList(l2))
