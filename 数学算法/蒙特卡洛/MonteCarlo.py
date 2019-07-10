import random

def run():
	n = 10**4
	n_pai = 0
	for i in range(1, n + 1):
		x = random.random()
		y = random.random()
		
		# 落在单位圆内部
		if x**2 + y**2 <= 1:
			n_pai = n_pai + 1

	pai = n_pai / float(n) * 4

	print(pai)


if __name__ == '__main__':
	run()