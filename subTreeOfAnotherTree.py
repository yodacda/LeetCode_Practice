class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class solution:
    def isSubTree(self, root:TreeNode, subRoot:TreeNode):
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return(self.isSubTree(root.left, subRoot) or
               self.isSubTree(root.right, subRoot))


    def isSameTree(self, r, s):
        if not r and not s:
            return True

        if s and r and r.val == s.val:
            return(self.isSameTree(r.left, s.left) and
                   self.isSameTree(r.right, s.right))

        return False

root = [3,4,5,1,2]
subRoot = [4,1,2]
obj = solution()
solution.isSubTree(obj, root, subRoot)