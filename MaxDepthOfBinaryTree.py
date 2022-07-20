from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class solution:

    ####1st Method

    def maxDepthTree1(self, root:TreeNode):
        if not root:
            return 0

        return 1 + max(self.maxDepthTree(root.left), self.maxDepthTree(root.right))

    ####2nd Method BFS Model Breadth First Search Model
    def maxDepthTree2(self, root:TreeNode):
        if not root:
            return 0

        q = deque([root])
        level = 0

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return level


    ####3rd Method Iterative DFS Depth First Search method.
        def maxDepthTree3(self, root:TreeNode):
            stack = [[root, 1]]
            res = 0

            while stack:
                node, depth = stack.pop()

                if node:
                    res = max(res, depth)
                    stack.append(node.left, depth + 1)
                    stack.append(node.right, depth + 1)

            return res
