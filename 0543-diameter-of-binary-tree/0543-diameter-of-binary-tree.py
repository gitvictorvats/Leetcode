# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def calulateDepth(self,root):

            if root ==None:
                return 0

            return max(1+self.calulateDepth(root.right),1+self.calulateDepth(root.left))  

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if root==None:
            return 0

        # Diameter passing through root
        diameter_through_root = self.calulateDepth(root.right) + self.calulateDepth(root.left)
        
        # Diameter entirely in left subtree
        diameter_left = self.diameterOfBinaryTree(root.left)
        
        # Diameter entirely in right subtree
        diameter_right = self.diameterOfBinaryTree(root.right)
        
        # Return the maximum of the three possible diameters
        return max(diameter_through_root, diameter_left, diameter_right)


      
        