# Medium

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # root = None
        # for i in range(0, n, 1):
        #     root = insert(root, arr[i])
        # temp = Node(item)
        # if (root == None):
        #     root = temp
        # else :
        #     ptr = root
        #     while (ptr.next != None):
        #         ptr = ptr.next
        #     ptr.next = temp
    # return root

        if l1.val == 0 and l2.val == 0:
            print('')
        else:
            print(l1.val)


l1 = [2,4,3]
l2 = [5,6,4]
sol = Solution()
sol.addTwoNumbers(l1, l2)