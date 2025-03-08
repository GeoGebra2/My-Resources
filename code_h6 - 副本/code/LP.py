import newton as nt
import numpy as np
from copy import deepcopy


def centering_step(c, A, b, x0, t):
	"""
	c, A, b: parameters in LP

		min   c^T x
		s.t.  Ax = b
		      x >= 0

	x0: feasible initial point for constrained Newton's method
	t:  penalty parameter in barrier method

	This function returns the central point x^*(t) 
	"""
	#   START OF YOUR CODE
	def f(x):
		return c.T @ x - 1.0/t * sum(np.log(np.maximum(x, 1e-10)))
		#return c.T @ x - 1.0/t * sum(np.log(x))

	def fp(x):
		return c - 1.0/(t * x)

	def fpp(x):
		return np.diag((1.0/(x**2 * t)).T[0])
	
 
	return nt.newton_eq(f, fp, fpp, x0, A, b)[-1]
	

	#	END OF YOUR CODE


def barrier(c, A, b, x0, tol=1e-8, t0=1, rho=10):
	"""
	c, A, b: parameters in LP
	
		min   c^T x
		s.t.  Ax = b
		      x >= 0
		     
	x0:  feasible initial point for the barrier method
	tol: tolerance parameter for the suboptimality gap. The algorithm stops when

	         f(x) - f^* <= tol

	t0:  initial penalty parameter in barrier method
	rho: factor by which the penalty parameter is increased in each centering step

	This function should return a list of the iterates
	"""	
	t = t0
	x = np.array(x0)
	x_traces = [np.array(x0)]

	for it in range(1000):
		x1 = deepcopy(x)
		x = centering_step(c, A, b, x1, t)
		#print(x)
		#print(A@x==b)
		x_traces.append(deepcopy(x))
		#print(x)

        # 计算对偶间隙（这里是一个简单的示例计算）
		#lambda_ = np.linalg.lstsq(A.T, c, rcond = None)[0]
		#mu = 1 / t
		#gap = c.T @ x - b.T @ lambda_ - len(x) * mu

		if (1 / t) <= tol:
			break

		t = rho * t
	
	#	END OF YOUR CODE

	return x_traces