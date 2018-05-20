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

# def rootToLeafPaths(self, root):
#    if not root: return []
#    if not root.left and not root.right: return [str(root.val)]
#    return [str(root.val) + '->' + i for i in self.rootToLeafPaths(root.left)] +
#              [str(root.val) + '->' + i for i in self.rootToLeafPaths(root.right)]


    # def binaryTreePaths(self, root):
    #     if not root: return []
    #     result= [ str(root.val)+"->" + path for path in self.binaryTreePaths(root.left)]
    #     result+= [ str(root.val)+"->" + path for path in self.binaryTreePaths(root.right)]
    #     return result or [str(root.val)]  # if empty return leaf itself