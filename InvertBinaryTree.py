class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class solution:
    def invertTree(self, root:TreeNode):
        if not root:
            return None

        #swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        #recursively call the function by giving first child node values.
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root