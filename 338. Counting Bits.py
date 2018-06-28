class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # 0:0, 1:1                                                          [0,1]
        # 00:0, 01:1, 10:1, 11:2                                            [0,1,1,2]
        # 000:0, 001:1, 010:1, 011:2,   100:1, 101:2, 110:2, 111:3          [0,1,1,2,1,2,2,3]

        # Everytime, we consider last step's number as 0xyzzbc... , now we provide 1xyzabc..., so the number of 1s will be one more
        # A=A+[x+1  for x in A]

        A = [0, 1]
        while len(A) < num + 1:
            A += [a + 1 for a in A]
        return A[:num+ 1]

if __name__ == '__main__':
    num = 5
    print Solution().countBits(num)