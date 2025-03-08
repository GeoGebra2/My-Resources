import numpy as np
import copy

def gd_const_ss(fp, x0, stepsize, tol=1e-5, maxiter=100000):
	"""
	fp: function that takes an input x and returns the derivative of f at x
	x0: initial point in gradient descent
	stepsize: constant step size used in gradient descent
	tol: toleracne parameter in the stopping crieterion. Gradient descent stops 
	     when the 2-norm of the gradient is smaller than tol
	maxiter: maximum number of iterations in gradient descent.

	This function should return a list of the sequence of approximate solutions
	x_k produced by each iteration
	"""
	x_traces = [np.array(x0)]
	x = np.array(x0)
	#   START OF YOUR CODE
	for i in range(maxiter):
		x_grad = fp(x)
		if np.linalg.norm(x_grad) < tol:
			break
		x -= stepsize * x_grad
		x_traces.append(copy.deepcopy(x)) # record x
	#	END OF YOUR CODE

	return x_traces 

def gd_armijo(f, fp, x0, initial_stepsize=1.0, alpha=0.5, beta=0.5, tol=1e-5, maxiter=100000):
	"""
	f: function that takes an input x an returns the value of f at x
	fp: function that takes an input x and returns the derivative of f at x
	x0: initial point in gradient descent
	initial_stepsize: initial stepsize used in backtracking line search
	alpha: parameter in Armijo's rule 
				f(x - t * f'(x)) > f(x) - t * alpha * ||f'(x)||^2
	beta: constant factor used in stepsize reduction
	tol: toleracne parameter in the stopping crieterion. Gradient descent stops 
	     when the 2-norm of the gradient is smaller than tol
	maxiter: maximum number of iterations in gradient descent.

	This function should return a list of the sequence of approximate solutions
	x_k produced by each iteration and the total number of iterations in the inner loop
	"""
	x_traces = [np.array(x0)]
	stepsize_traces = []
	tot_num_inner_iter = 0

	x = np.array(x0)
	#   START OF YOUR CODE
	for i in range(maxiter):
		x_grad = fp(x)
		x_grad_norm = np.linalg.norm(x_grad) # record grad norm
		if(x_grad_norm < tol): break
		t = initial_stepsize
		while f(x - t*x_grad) > f(x) - alpha*t*(x_grad_norm**2):
			t *= beta
			tot_num_inner_iter += 1 # calculate the inner iterations running number
		stepsize_traces.append(copy.deepcopy(t)) # record stepsize after the update
		x -= t*x_grad
		x_traces.append(copy.deepcopy(x)) # record every x
		
	#	END OF YOUR CODE

	return x_traces, stepsize_traces, tot_num_inner_iter