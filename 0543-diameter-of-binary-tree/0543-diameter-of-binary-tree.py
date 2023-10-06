class Solution:
    
    def __init__(self):
        self.memo = {}

    def calulateDepth(self, root):
        if root == None:
            return 0

        if root in self.memo:
            return self.memo[root]

        left_depth = self.calulateDepth(root.left)
        right_depth = self.calulateDepth(root.right)
        
        # Store the computed depth in the memo dictionary
        self.memo[root] = 1 + max(left_depth, right_depth)
        
        return self.memo[root]

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        # Diameter passing through root
        diameter_through_root = self.calulateDepth(root.right) + self.calulateDepth(root.left)

        # Diameter entirely in left subtree and right subtree
        diameter_left = self.diameterOfBinaryTree(root.left)
        diameter_right = self.diameterOfBinaryTree(root.right)

        # Return the maximum of the three possible diameters
        return max(diameter_through_root, diameter_left, diameter_right)
