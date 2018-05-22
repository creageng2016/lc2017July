

class Solution(object):
	def hIndex(self, citations):
		"""
		:type citations: List[int]
		:rtype: int
		"""
		citations.sort()

		for i in range(len(citations)):
			# _c = citations[len(citations) - i - 1]
			h = len(citations) - i 
			if citations[i] >= h:
				return h
		return 0

	# def hIndex(self, citations):
		# 	citations.sort()
		# 	n = len(citations)
		# 	for i in xrange(n):
		# 		if citations[i] >= (n-i):
		# 			return n-i
		# 	return 0

if __name__ == '__main__':
	citations = [3,0,6,1,5]
	print Solution().hIndex(citations)        