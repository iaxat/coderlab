# Medium
# from create_linkedLIst import ListNode

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        
        
        
        # prehead = ListNode(-1)
        # val_count = ListNode(0)
        # prev = prehead
        # if l1 is None:
        #     return l2
        # if l2 is None:
        #     return l1
        # while l1 and l2:
        #     # count_extra = 0
        #     val_count.val = l1.val + l2.val
        #     prev.next = val_count
        #     l1 = l1.next
        #     l2 = l2.next
        #     prev = prev.next

        # prev.next = l1 if l1 is not None else l2

        # while prehead.next is not None:
        #     prehead = prehead.next
        #     print(prehead.val)
        # return prehead.next


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
