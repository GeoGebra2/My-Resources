import time

# a = 12345678987654321
# n = 12345678987654321
# p = 0XFFFFFFFF

a = 2
n = 123456789
p = 0XFFFFFFFF

print(f"a={a}, n={n}, p={p}")

def test_naive_pow(a, n, p):
	time_begin = time.time()
	print("Naive pow: the answer is", a**n%p)
	time_end = time.time()
	print("    The time is {}".format(time_end-time_begin))  

#test_naive_pow(a=2, n=1234567890, p=0XFFFFFFFF)

#test_naive_pow(a=2, n=123456789, p=0XFFFFFFFF)

def test_pow_v1(a, n, p):
	time_begin = time.time()

	ans = 1
#	for _ in range(n):
	i = 0
	while i<n:
		ans = (ans*a)%p
		i += 1

	print("Loop pow: the answer is", ans)
	time_end = time.time()
	print("    The time is {}".format(time_end-time_begin))  

#test_pow_v1(a=2, n=1234567890, p=0XFFFFFFFF)

#test_pow_v1(a=2, n=123456789, p=0XFFFFFFFF)

def fast_pow(a, n, p):
	if n == 0:
		return 1

	x = fast_pow(a, n//2, p)
	if n%2 == 0:
		return x*x % p

	return x*x * a % p


def test_pow_v2(a, n, p):
	time_begin = time.time()

	ans = fast_pow(a, n, p)
	print("Fast pow: the answer is", ans)
	
	time_end = time.time()
	print("    The time is {}".format(time_end-time_begin))

test_pow_v2(a=2, n=123456789, p=0XFFFFFFFF)


def fast_pow_no_recursion(a, n, p):

	ans = 1
	e = a % p

	while n>0:
		if n%2 == 1:
			ans = (ans * e) % p

		e = (e * e) % p
		n //= 2

	return ans


def test_pow_v3(a, n, p):
	time_begin = time.time()

	ans = fast_pow_no_recursion(a, n, p)
	print("Fast pow (no recursio): the answer is", ans)
	time_end = time.time()
	print("    The time is {}".format(time_end-time_begin))

test_pow_v3(a=2, n=123456789, p=0XFFFFFFFF)


def test_pow(a, n, p):
	time_begin = time.time()

	print("Pow(): the answer is", pow(a, n, p))
	time_end = time.time()
	print("    The time is {}".format(time_end-time_begin))

test_pow(a=2, n=123456789, p=0XFFFFFFFF)

import math
def test_mathpow(a, n, p):
	time_begin = time.time()

	print("math.pow: The answer is", math.pow(a, n)%p)
	time_end = time.time()
	print("    The time is {}".format(time_end-time_begin))

# test_mathpow(a=2, n=123456789, p=0XFFFFFFFF) error math.pow overflow
a = 2
n = 123
p = 0XFFFFFFFF
print(f"a={a}, n={n}, p={p}")
test_mathpow(a=2, n=123, p=0XFFFFFFFF)
test_pow(a=2, n=123, p=0XFFFFFFFF)