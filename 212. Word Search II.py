

class Solution(object):
	def findWords(self, board, words):
		"""
		:type board: List[List[str]]
		:type words: List[str]
		:rtype: List[str]
		"""
		trie = {}
		for word in words:
			t = trie
			for c in word:
				if c not in t:
					t[c] = {}
				t = t[c]
			t["#"] = "#"

		res = []
		m   = len(board)
		n   = len(board[0])
		
		def find(i, j, trie, path):
			if "#" in trie:
				res.append(path)

			if i < 0 or j < 0 or i >= m or j >= n:
				return 

			tmp = board[i][j]
			if tmp not in trie:
				return 

			board[i][j] = "@"
			find(i - 1, j, trie[tmp], path + tmp)
			find(i + 1, j, trie[tmp], path + tmp)
			find(i, j - 1, trie[tmp], path + tmp)
			find(i, j + 1, trie[tmp], path + tmp)
			board[i][j] = tmp

		for i in range(m):
			for j in range(n):
				find(i, j, trie, '')
		res = list(set(res))
		return res


if __name__ == '__main__':
	words = ["oath","pea","eat","rain"]
	board = [
				['o','a','a','n'],
				['e','t','a','e'],
				['i','h','k','r'],
				['i','f','l','v']
			]


	print Solution().findWords(board, words)


		# trie = {}
		# for word in words:
		#     t = trie
		#     for c in word:
		#         if c not in t:
		#             t[c] = {}
		#         t = t[c]
		#     t["#"] = "#"

		# res = []
		# m   = len(board)
		# n   = len(board[0])

		# def find(i, j, path, trie):
		#     if "#" in trie:
		#         res.append(path)
			
		#     if i < 0 or j < 0 or i >= m or j >= n:
		#         return 
		#     tmp         = board[i][j]
			
		#     if tmp not in trie:
		#         return 
			
		#     board[i][j] = "@"

		#     find(i + 1, j, path + tmp, trie[tmp])
		#     find(i - 1, j, path + tmp, trie[tmp])
		#     find(i, j - 1, path + tmp, trie[tmp])
		#     find(i, j + 1, path + tmp, trie[tmp])

		#     board[i][j] = tmp

		# for i in range(m):
		#     for j in range(n):
		#         find(i, j, '', trie)

		# return list(set(res))    