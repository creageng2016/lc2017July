import bisect
class Solution(object):
	def maxEnvelopes(self, envelopes):
			"""
			:type envelopes: List[List[int]]
			:rtype: int
			"""
			envelopes = sorted(envelopes, 
								cmp = lambda x, y: x[0] - y[0]    \
									if x[0] != y[0]               \
									else y[1] - x[1]              \
								)
			# print envelopes
			res = self.findLongestInc(map(lambda x: x[1], envelopes))
			return len(res)

	def findLongestInc(self,envelopes):
			array = []
			for env in envelopes:
				pos = bisect.bisect_left(array, env)
				if pos == len(array):
					array.append(env)
				else:
					array[pos] = env
			return array



if __name__ == '__main__':
	envelopes = [[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]
	print Solution().maxEnvelopes(envelopes)