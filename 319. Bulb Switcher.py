
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(n ** 0.5)
        
        # if n == 0:
        # 	return 0
        # if n == 1:
        # 	return 1

        # k = n
        # lights = [False for i in range(n)]
        # step = 0

        # while n:
        # 	step += 1
        # 	for i in range(step - 1, k, step):
        # 		lights[i] = not lights[i]
        # 	# print step, lights
        # 	n -= 1
        # return sum(lights)





if __name__ == '__main__':
	n = 3

	print Solution().bulbSwitch(n)