import collections

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
        	return False
        if s == t:
        	return False

        return collections.Counter(s) == collections.Counter(t)




if __name__ == '__main__':
	s = "anagram"
	t = "nagaram"
	print Solution().isAnagram(s, t)        