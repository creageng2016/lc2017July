import bisect

class Solution(object):
	def maxEnvelopes(self, envelopes):
			"""
			:type envelopes: List[List[int]]
			:rtype: int
			"""
			envelopes = sorted(envelopes, 
								cmp = lambda x, y: x[0] - y[0]  \
									if x[0] != y[0]               \
									else y[1] - x[1]              \
								)
			# print envelopes
			res = self.findLongestInc(envelopes)
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
	# envelopes =  [[5,4],[6,4],[6,7],[2,3]]
	envelopes = [[3,4],[1,2],[2,3],[4,5],[5,6],[5,5],[6,7],[7,8]]
	# ([2,3] => [5,4] => [6,7])
	#  3
	print (Solution().maxEnvelopes(envelopes))



		#     if not envelopes:
		#         return 0
		#     envelopes.sort(key=lambda c:(c[0],-c[1]))
		#     return self.longestSubsequece(list(map(lambda c: c[1], envelopes)))

		# def longestSubsequece(self, arr):
		#     q = []
		#     for i in arr:
		#         pos = bisect.bisect_left(q, i)
		#         if len(q) == pos:
		#             q.append(i)
		#         else:
		#             q[pos] = i
		#     return len(q)


				# if len(envelopes) == 0:
				# 	return 0

				# for e in envelopes:
				# 	if e[0] > e[1]:
				# 		e[0], e[1] = e[1], e[0]
				
				# envelopes = sorted(envelopes, key = lambda x: (x[0], x[1]))
				# myenvelopes = []
				# myenvelopes.append(envelopes[0])

				# for i in range(1, len(envelopes)):
				# 	if envelopes[i] != envelopes[i - 1]:
				# 		myenvelopes.append(envelopes[i])

				# dp = [0 for i in range(len(myenvelopes))]
				# dp[0] = 1

				# for i in range(1, len(myenvelopes)):
				# 	if myenvelopes[i][0] > myenvelopes[i - 1][0] \
				# 		and myenvelopes[i][1] > myenvelopes[i - 1][1] \
				# 		and myenvelopes[i][0] > myenvelopes[i -1][1]:
				# 		dp[i] = dp[i - 1] + 1
				# 	else:
				# 		dp[i] = dp[i -2] + 1
				# print (myenvelopes)
				# return dp[-1]
