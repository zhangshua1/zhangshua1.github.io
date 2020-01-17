import time
def work_a(a):
	for var in range(100000):
		a[0] += 1
def work_b(a):
	for var in range(100000):
		a[0] = a[0] * 2

def work_c(a):
	for var in range(1000000):
		a[0] = a[0] - 2

a = [1]
start = time.time()
work_a(a)
print('-------')
work_b(a)
print('-------')
work_c(a)
print('-------')
end = time.time()
print('程序耗时：%.2f' % (end - start))
