class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # res     = 0
        opt     = "+"
        i       = 0
        curr    = 0
        stack   = []
        
        while i < len(s):
            # print stack
            if s[i].isdigit():
                curr = s[i]
                while i + 1 < len(s) and s[i + 1].isdigit():
                    curr += s[i + 1]
                    i += 1
            if s[i] != " " or i == len(s) - 1:
                if opt == "+":
                    stack.append(int(curr))
                elif opt == "-":
                    stack.append(-int(curr))
                elif opt == "*":
                    stack.append(stack.pop() * int(curr))
                elif opt == "/":
                    stack.append(stack.pop() / int(curr))
                opt = s[i]
                curr = 0
            i += 1

        res = sum(stack)
        return res
                
if __name__ == '__main__':
    s = " 3+5 / 2 "
    print Solution().calculate(s)                
                
        