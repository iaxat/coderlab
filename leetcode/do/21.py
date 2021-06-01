# Easy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
        print(l1,l2)

l1 = [1,2,4]
l2 = [1,3,4]
sol=Solution()
sol.mergeTwoLists()