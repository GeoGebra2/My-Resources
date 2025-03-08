import numpy as np
from copy import deepcopy

def newton_eq(f, fp, fpp, x0, A, b, initial_stepsize=1.0, alpha=0.5, beta=0.5, tol=1e-5, maxiter=1000):
	"""
	f: function that takes an input x an returns the value of f at x
	fp: function that takes an input x and returns the gradient of f at x
	fpp: function that takes an input x and returns the Hessian of f at x
	A, b: constraint A x = b
	x0: initial feasible point
	initial_stepsize: initial stepsize used in backtracking line search
	alpha: parameter in Armijo's rule 
				f(x + t * d) > f(x) + t * alpha * f(x) @ d
	beta: constant factor used in stepsize reduction
	tol: toleracne parameter in the stopping crieterion. Gradient descent stops 
	     when the 2-norm of the Newton direction is smaller than tol
	maxiter: maximum number of iterations in outer loop of damped Newton's method.

	This function should return a list of the iterates x_k
	"""
	x_traces = [np.array(x0)]
	
	x = np.array(x0)

	for it in range(maxiter):
	#   START OF YOUR CODE
		lamada = -np.linalg.inv(A @ np.linalg.inv(fpp(x)) @ A.T) @ (A @ np.linalg.inv(fpp(x)) @ fp(x))
		v = -np.linalg.inv(fpp(x)) @ (fp(x) + A.T @ lamada)

		stepsize = initial_stepsize
		while f(x + stepsize * v) > f(x) + alpha * stepsize * (fp(x).T) @ v:
			stepsize *= beta

		x += stepsize * v
		x_traces.append(deepcopy(x))

		if np.linalg.norm(v) <= tol: break
	#	END OF YOUR CODE

	return x_traces

def gd_const_ss(fp, x0, stepsize, tol=1e-5, maxiter=100000):
    """
    fp: function that takes an input x and returns the derivative of f at x
    x0: initial point in gradient descent
    stepsize: constant step size used in gradient descent
    tol: toleracne parameter in the stopping criterion. Gradient descent stops 
         when the 2-norm of the gradient is smaller than tol
    maxiter: maximum number of iterations in gradient descent.

    This function should return a list of the sequence of approximate solutions
    x_k produced by each iteration
    """
    x_traces = [np.array(x0)]
    x = np.array(x0)
    for _ in range(maxiter):
        derivative = fp(x)
        if np.linalg.norm(derivative) < tol:
            #print("iteration: ", i)
            break
        x = x - stepsize * derivative
        x_traces.append(x)
    return x_traces

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