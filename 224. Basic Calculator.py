class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign    = 1
        accSum = 0
        stack   = []
        i = 0
        while i < len(s):
            # while i < len(s) and s[i] == " ":
            #     i += 1
            if s[i].isdigit():
                curr = s[i]
                while i + 1 < len(s) and s[ i+ 1].isdigit():
                    curr += s[i+1]
                    i += 1
                accSum += sign * int(curr)  
            
            elif s[i] == "(":
                    stack.append(accSum)
                    stack.append(sign)
                    accSum = 0
                    sign = 1
            elif s[i] == ")":
                    _sign  = stack.pop()
                    _res   = stack.pop()
                    accSum = _sign * accSum + _res
            elif s[i] == "+":
                sign = 1
            elif s[i] == "-":
                sign = -1
            i += 1
        return accSum
                      
if __name__ == '__main__':
    s = "(1+(4+5+2)-3)+(6+8)"
    print Solution().calculate(s)