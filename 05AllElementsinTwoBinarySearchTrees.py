'''Given two binary search trees root1 and root2.
Return a list containing all the integers from both trees sorted in ascending order.

Example 1:
   2       1
  / \     / \
 1   4   0   3
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]

Example 3:
Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]

Example 4:
Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]

Example 5:
   1       8
    \     / 
     8   1   
Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(root, arr):
            if root==None:
                return
            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right, arr)
        l = list()
        inorder(root1, l)
        inorder(root2, l)
        return sorted(l)
