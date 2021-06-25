# # Easy

# # Definition for singly-linked list.
class LIST_:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: LIST_, l2: LIST_) -> LIST_:
    	l1.next = l2.val


l1 = [1,2,4], l2 = [1,3,4]
sol = Solution()
sol.mergeTwoLists(l1,l2)


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
