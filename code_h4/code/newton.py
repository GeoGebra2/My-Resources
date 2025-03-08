import numpy as np

def newton(fp, fpp, x0, tol=1e-5, maxiter=100000):
	"""
	fp: function that takes an input x and returns the gradient of f at x
	fpp: function that takes an input x and returns the Hessian of f at x
	x0: initial point  
	tol: toleracne parameter in the stopping criterion. Newton's method stops 
	     when the 2-norm of the gradient is smaller than tol
	maxiter: maximum number of iterations

	This function should return a list of the sequence of approximate solutions
	x_k produced by each iteration
	"""
	x_traces = [np.array(x0)]
	x = np.array(x0)
	#   START OF YOUR CODE

	for _ in range(maxiter):
		grad = np.array(fp(x))
		hessian = np.array(fpp(x))
		if np.linalg.norm(grad) < tol:
			break
		step = np.linalg.solve(hessian, -grad)
		x = x + step
		x_traces.append(x)

	#	END OF YOUR CODE

	return x_traces 

