import re
import operator

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        patttern    = re.compile(r'\s+')
        input       = re.sub(patttern, '', input) 

        token   = re.split("(\D)", input)
        # print token
        nums    = map(int, token[::2])
        # print nums
        ops     = map( {"+":    operator.add, 
                        "-":    operator.sub,
                        "*":    operator.mul}.get,
                    token[1:-1:2]
            )
        # print ops
        def build(lo, hi):
            if lo == hi:
                return [nums[lo]]
            return [ops[i](a, b) 
                    for i in xrange(lo, hi)
                    for a in build(lo,i)
                    for b in build(i + 1, hi)
                ]
        return build(0, len(nums) - 1)


if __name__ == '__main__':
    input = "2  *3-4*5"
    print Solution().diffWaysToCompute(input)