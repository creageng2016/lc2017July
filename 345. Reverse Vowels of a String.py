


class Solution(object):
	def reverseVowels(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		
		vowels = 'aeiouAEIOU'
		ix = []
		appeared = []

		slist = list(s)

		for i, c in enumerate(slist):
			if c.lower() in vowels:
				ix.append(i)
				appeared.append(c)

		appeared = appeared[::-1]
		for i in ix:
			slist[i] = appeared.pop(0)

		return ''.join(slist)


if __name__ == '__main__':
	s = "leetcode"
	print Solution().reverseVowels(s)