

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return

        m = len(board)
        n = len(board[0])

        tmp = board.copy()
        print tmp
        for i in range(m):
            for j in range(n):
                nbs = []
                print "i %s j %s >>>" %(i, j)
                if i > 0:
                    nbs.append(board[i - 1][j])
                    if j > 0: nbs.append(board[i - 1][j - 1])
                    if j < n - 1: 
                        print  "22", i - 1, j + 1
                        print board[i - 1][j + 1]
                        nbs.append(board[i - 1][j + 1])
                
                if i < m - 1:
                    nbs.append(board[i + 1][j])
                    if j > 0: nbs.append(board[i + 1][j - 1])
                    if j < n - 1:
                        nbs.append(board[i + 1][j + 1])
                
                if j > 0:
                    nbs.append(board[i][j - 1])             
                if j < n - 1:
                    nbs.append(board[i][j + 1])

                nblives = sum(nbs)
                nbdead = len(nbs) - nblives


                if board[i][j]:
                    if nblives < 2:
                        board[i][j] = 0
                    elif nblives in [2, 3]:
                        board[i][j] = 1
                    elif nblives > 3:
                        board[i][j] = 0
                else:
                    if nblives == 3:
                        board[i][j] = 1

        print board



if __name__ == '__main__':
    board = [[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
    print board[1][2]


    print Solution().gameOfLife(board)