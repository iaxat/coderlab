# Medium
# from create_linkedLIst import ListNode

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # method 1 
        a = []
        b = []
        sum = 0

        while l1:
            a.append(l1.val)
            l1 = l1.next
        while l2:
            b.append(l2.val)
            l2 = l2.next
        
        stack = []
        for i in a:
            stack.append(str(i))
        stack = stack[::-1]
        a = ''.join(stack)
        a = int(a)

        stack = []
        for i in b:
            stack.append(str(i))
        stack = stack[::-1]
        b = ''.join(stack)
        b = int(b)

        sum = a + b
        sum = str(sum)
        sum = sum[::-1]

        result = [int(i) for i in sum]

        list_head = ListNode()
        prev = list_head
        for i in result:
            a = ListNode(i)
            prev.next=a
            prev = prev.next

        # return list_head.next


        # method 2
        # using carry over
        prehead_return = ListNode()
        while l1 and l2:
            print('')
            

    

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
print(sol.addTwoNumbers(create_linkedList(l1), create_linkedList(l2)))
