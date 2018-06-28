class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m   = len(matrix)
        if m == 0:
            return 0
        n   = len(matrix[0])
        ml  = 0

        cache = [[0]*n for _ in range(m)]
        
        def dfs(i, j):
            tmp = matrix[i][j]
            # print matrix, i, j

            if matrix[i][j] == -1:
                return 0
            if cache[i][j]:
                return cache[i][j]

            matrix[i][j] = -1
            a = b = c = d = 0
            # left
            if j > 0 and matrix[i][j - 1] > tmp:
                a = dfs(i, j - 1) + 1

            # right:
            if j < n - 1 and matrix[i][j + 1] > tmp:
                b = dfs(i, j + 1) + 1

            # top
            if i > 0 and matrix[i - 1][j] > tmp:
                c = dfs(i - 1, j) + 1
            
            # bottom
            if i < m - 1 and matrix[i + 1][j] > tmp:
                d = dfs(i + 1, j) + 1

            matrix[i][j] = tmp
            res = max(a,b,c,d, 1)
            cache[i][j] = res
            return res
            # return pathlen
        for i in range(m):
            for j in range(n):
                # print matrix
                ml = max(ml, dfs(i, j))
        return ml

# Top-down DP, about 560 ms.
def longestIncreasingPath(self, matrix):
    def length(z):
        if z not in memo:
            memo[z] = 1 + max([length(Z)
                               for Z in z+1, z-1, z+1j, z-1j
                               if Z in matrix and matrix[z] > matrix[Z]]
                               or [0])
        return memo[z]

    memo = {}
    matrix = {i + j*1j: val
              for i, row in enumerate(matrix)
              for j, val in enumerate(row)}
    return max(map(length, matrix) or [0])


if __name__ == '__main__':
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    # 4
    print Solution().longestIncreasingPath(matrix)