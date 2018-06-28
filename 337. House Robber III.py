



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):

        cache = {}

        def dfs(root, cache):

            if not root:
                return 0
        
            if root in cache:
                return cache[root]

            path1 = dfs(root.left, cache) + dfs(root.right, cache)

            #path2
            grand_left = grand_right = 0
            if root.left:
                grand_left = dfs(root.left.left, cache) + dfs(root.left.right, cache)
            
            if root.right:
                grand_right = dfs(root.right.left, cache) + dfs(root.right.right, cache)

            path2 = root.val + grand_left + grand_right

            res = max(path1, path2)
            cache[root] = res
        
            return res

        return dfs(root, cache)


    #   """
    #   :type root: TreeNode
    #   :rtype: int
    #   """
    #   # path1

    #   return self.dfs(root)[0]

    # def dfs(self, root):
    #   if not root:
    #       return 0, 0

    #   rob_L, no_rob_L = self.dfs(root.left)
    #   rob_R, no_rob_R = self.dfs(root.right)

    #   return max(roo.val + no_rob_L + no_rob_R, rob_L + rob_R), rob_L + rob_R