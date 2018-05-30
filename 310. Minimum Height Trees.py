class Solution(object):
	def findMinHeightTrees(self, n, edges):
		"""
		:type n: int
		:type edges: List[List[int]]
		:rtype: List[int]
		"""
		import collections
		indegree 	= [0 for i in range(n)]
		gr 			= collections.defaultdict(list)
		
		# if not edges:
		# 	return [0]
		
		for u, v in edges:
			gr[u].append(v)
			gr[v].append(u)
			indegree[u] += 1
			indegree[v] += 1

		leaves 		= [i for i in range(n) if indegree[i] == 1]
		# print leaves
		while leaves and len(gr) > 2:
			nextleaves = []
			for leave in leaves: 
				nextnodes = gr.pop(leave)
				for nextn in nextnodes:
					indegree[nextn] -= 1
					if indegree[nextn] == 1:
						nextleaves.append(nextn)

			leaves = nextleaves
		return gr.keys() or [0]



if __name__ == '__main__':
	n = 1
	# edges = [[1, 0], [1, 2], [1, 3]]
	edges = []
	# edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
	print Solution().findMinHeightTrees(n, edges)

		
		
	
		