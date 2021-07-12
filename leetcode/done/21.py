# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        prehead = ListNode(-1)
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next
        prev.next = l1 if l1 is not None else l2

        while prehead.next is not None:
            prehead = prehead.next
            print(prehead.val)
        return prehead.next

    # recursion linked list process
    def mergeList_recursion(self, l1:ListNode, l2:ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        





l1 = [1,2,4]
l2 = [1,3,4]
sol = Solution()

def create_linkedList(data):
    list_head = ListNode()
    prev = list_head
    for i in data:
        a = ListNode(i)
        prev.next=a
        prev = prev.next

    return list_head.next

sol.mergeTwoLists(create_linkedList(l1),create_linkedList(l2))
sol.mergeList_recursion(create_linkedList(l1),create_linkedList(l2))
