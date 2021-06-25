# # Easy

# # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		new_head = ListNode()
		new_head.next = l1
		l1.next = l2


l1 = [1,2,4], l2 = [1,3,4]
sol = Solution()
print(sol.mergeTwoLists(l1,l2))


# # Node class
# class Node:
# 	# Function to initialize the node object
# 	def __init__(self, data):
# 		self.data = data # Assign data
# 		self.next = None # Initialize
# 						# next as null

# # Linked List class
# class LinkedList:
# 	# Function to initialize the Linked
# 	# List object
# 	def __init__(self):
# 		self.head = None
