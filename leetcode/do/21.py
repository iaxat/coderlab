# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def head_node (self):
        self.head = None

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        



l1 = [1,2,4]
l2 = [1,3,4]
sol = Solution()
sol.mergeTwoLists(ListNode(l1),ListNode(l2))
