"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []

"""

class TreeNode(object):
    def __init__(self, val):
        self.val =val
        self.next = None

def mergeKsorted(lists):
    if len(lists) == 0:
            return None
    
    if len(lists) == 1:
        return lists[0]
    
    low = 0
    high = len(lists)

    mid =(high - low) // 2

    left = mergeKsorted(lists[:mid])
    right = mergeKsorted(lists[mid:])

    return merge(left, right)

def merge(left, right):
    dummyNode = TreeNode()
    tail = dummyNode

    curr1 = left
    curr2 = right

    while True:

        if curr1 is None:
            tail.next = curr2
            break
        if curr2 is None:
            tail.next = curr1
            break

        if curr1.val <= curr2.val:
            tail.next = curr1
            curr1 = curr1.next
        else:
            tail.next = curr2
            curr2 = curr2.next

        tail = tail.next
    

    return dummyNode.next