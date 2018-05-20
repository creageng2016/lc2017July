# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        
        def dfs(node, path):
            if not node.left and not node.right:
                path += [node.val]
                res.append(path)
                return
            if node.left:
                dfs(node.left, path + [node.val])
            if node.right:
                dfs(node.right, path + [node.val])
        dfs(root, [])
        # print res
        res = ["->".join([str(v) for v in path]) for path in res]
        return res