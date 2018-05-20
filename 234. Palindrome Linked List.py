# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def isPalindrome(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		""" 
		rev = None
		fast = slow = head

		while fast and fast.next:
			fast = fast.next.next

			rev, rev.next, slow = slow, rev, slow.next
		
		if fast:
			slow = slow.next

		while slow and rev:
			if slow.val != rev.val:
				return False
			slow 	= slow.next
			rev 	= rev.next

		return True



if __name__ == '__main__':
	head = None
	print Solution().isPalindrome(head)