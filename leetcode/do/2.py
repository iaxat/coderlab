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
        while l1:
            a.append(l1.val)
            l1 = l1.next
        while l2:
            b.append(l2.val)
            l2 = l2.next
        
        stack = []
        for i in a:
            stack.push(str(i))

        a = ''.join(stack)
        a = int(a)

        stack = []
        for i in b:
            stack.append(str(i))
        b = ''.join(stack)
        b = int(b)


        print(a, ' ', b)
    

l1 = [2,4,3]
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
