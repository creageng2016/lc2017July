class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """


       	# length = len(s1)
       	# dp = [[False for j in range(length)] for i in range(length)
        
        # 
        l1 = list(s1)
        l1.sort()

        l2 = list(s2)
        l2.sort()

        if s1 == s2:
        	return True

        if l1 != l2:
        	return False

        n = len(s1)
        for i in range(1, n):
        	if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
        		return True
        	if self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i]):
        		return True
        return False
