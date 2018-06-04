# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def kthSmallest(self, root, k):
		"""
		:type root: TreeNode
		:type k: int
		:rtype: int
		"""
		stack = []
		# stack.append(root)

		while stack:
			# curr = stack.pop()
			if curr.left:
				stack.append(curr.left)
				curr = curr.left
			else:
				k -= 1
				if k == 0:
					return curr
				curr = curr.right


class Solution(object):
    def inorderTraversal(self, root):
        nodeval = []
        curr = root
        stack = []

        while curr or len(stack) != 0 :
            if curr is None:
                curr = stack.pop()
                nodeval.append(curr.val)
                curr = curr.right
            else:
                stack.append(curr)
                curr = curr.left

        return nodeval

	# stack = []
 #        while(root or len(stack)>0):
 #            while(root):
 #                stack.append(root);
 #                root = root.left
 #            top = stack.pop()
 #            k = k - 1
 #            if( k == 0):
 #                return top.val
 #            root = top.right



		