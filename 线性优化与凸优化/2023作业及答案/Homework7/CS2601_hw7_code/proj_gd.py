import numpy as np
from copy import deepcopy

def proj_gd(fp, proj, x0, stepsize, tol=1e-5, maxiter=100000):
	"""
	projected gradient descent for minimizing f(x) over X

	fp: function that takes an input x and returns the derivative of f at x
	proj: projection operator takes x as input and outputs its projection onto X 
	x0: initial point
	stepsize: constant step size used in gradient descent
	tol: toleracne parameter in the stopping crieterion. 
	     Projected gradient descent stops when ||x_{k+1} - x_k|| < t * tol
	maxiter: maximum number of iterations in gradient descent.

	This function should return the sequence of approximate solutions x_k 
	produced by each iteration, and also the sequence y_k before projection
	"""
	x_traces = [np.array(x0)]
	y_traces = []
	x = np.array(x0)

	for k in range(maxiter):
	#   START OF YOUR CODE
		x1 = x
		x_grad = fp(x1)
		y_traces.append(deepcopy(x_grad)) # y is output of gradient step before projection
		x = proj(x1 - stepsize * x_grad)
		x_traces.append(np.array(deepcopy(x)))
		if np.linalg.norm(x - x1) < stepsize * tol: break
		
	#	END OF YOUR CODE
	return x_traces, y_traces