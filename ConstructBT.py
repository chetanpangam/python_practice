"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree 
and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructBT(preorder, inorder):
    
    if not preorder or not inorder:
        return None
    
    mid = inorder.index(preorder[0])
    root = TreeNode(mid)

    root.left = constructBT(preorder[1:mid+1], inorder[:mid])
    root.right = constructBT(preorder[mid+1:], inorder[mid+1:])
    
    return root