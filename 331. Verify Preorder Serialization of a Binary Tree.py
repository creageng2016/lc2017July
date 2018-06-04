class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack =[]
        preorderlist = preorder.split(",")
        
        for c in preorderlist:
            if c != "#":
                stack.append(c)
            else:
                stack.append("#")
                while len(stack) >= 2 and stack[-1] == stack[-2] == "#":
                    stack.pop()
                    stack.pop()
                    if stack:
                        stack[-1] = "#"
                    else:
                        return False
        return True if len(stack) == 1 and stack[-1] == "#" else False
 


if __name__ == '__main__':
    # preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    preorder = "1,#,#,#,#"
    print Solution().isValidSerialization(preorder)        