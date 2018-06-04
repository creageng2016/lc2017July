

class Solution(object):
	def maxProduct(self, words):
		"""
		:type words: List[str]
		:rtype: int
		"""
		# bits = [0 for i in range(len(words))]

		# for i in range(len(words)):
		# 	val = 0
		# 	for j in range(len(words[i])):




		# pro = 0
		# for i in range(len(words) - 1):
		# 	for j in range(len(words)):
		# 		if not set(list(words[i])) & set(list(words[j])):
		# 			pro  = max(pro, len(words[i]) * len(words[j]))
		# return pro


class Solution(object):
    def maxProduct(self, words):
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - 97))
            d[mask] = max(d.get(mask, 0), len(w))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])


if __name__ == '__main__':
	words = ["abcw","baz","foo","bar","xtfn","abcdef"]
	# 16
	print Solution().maxProduct(words)