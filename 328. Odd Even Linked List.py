# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """        
        evenHead        = ListNode(0)
        oddHead         = ListNode(0)

        oddHead.next    = head
        evenHead.next   = None
        currEven        = evenHead
        currOdd         = oddHead
    
        oddflag = True
        while head:
            if oddflag:
                currOdd.next = head
                currOdd = currOdd.next
            else:
                currEven.next = head
                currEven = currEven.next
            oddflag  = not oddflag
            head = head.next
            # print head.val
        print currOdd.val
        print currEven.val
        currOdd.next = evenHead.next
        currEven.next = None
        return oddHead.next



        