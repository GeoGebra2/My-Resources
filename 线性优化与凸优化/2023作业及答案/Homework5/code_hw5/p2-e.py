import numpy as np
import newton
import utils
import matplotlib.pyplot as plt


def f(x):
	return f_2d(x[0], x[1])

def fp(x):
	#   START OF YOUR CODE
	return np.array([np.exp(x[0] + 3*x[1] - 0.1) + np.exp(x[0] - 3*x[1] - 0.1) - np.exp(-x[0] - 0.1),
                  3*np.exp(x[0] + 3 * x[1] - 0.1) - 3*np.exp(x[0] - 3*x[1] - 0.1)])
	#	END OF YOUR CODE

def fpp(x):
	#   START OF YOUR CODE
	a = np.array([np.exp(x[0] + 3*x[1] - 0.1) + np.exp(x[0] - 3*x[1] - 0.1) + np.exp(-x[0] - 0.1), 
               3*np.exp(x[0] + 3 * x[1] - 0.1) - 3*np.exp(x[0] - 3*x[1] - 0.1)])
	b = np.array([3*np.exp(x[0] + 3 * x[1] - 0.1) - 3*np.exp(x[0] - 3*x[1] - 0.1),
                9*np.exp(x[0] + 3*x[1] - 0.1) + 9*np.exp(x[0] - 3*x[1] - 0.1)])
	
	return np.array([a, b])
	#	END OF YOUR CODE

def f_2d(x1, x2):
	return np.exp(x1+3*x2-0.1) + np.exp(x1 - 3*x2 - 0.1) + np.exp(-x1-0.1)

# use the value you find in HW7
f_opt = 2.55926

def gap(x):
	return f(x) - f_opt

x0 = np.array([2.5,1.0])
path = 'figures/2e/'

#### Newton
x_traces = newton.newton(fp, fpp, x0)
f_value= f(x_traces[-1])


print()
print("Newton's method")
print('  number of iterations:', len(x_traces)-1)
print('  solution:', x_traces[-1])
print('  value:', f_value)

utils.plot_traces_2d(f_2d, x_traces, path+'nt_traces.jpg')
utils.plot(gap, x_traces, path+'nt_gap.jpg')