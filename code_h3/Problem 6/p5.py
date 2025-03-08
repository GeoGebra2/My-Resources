import numpy as np
import gd
import utils


#gamma = 
X = np.array([[2.0,0.0],[0.0,1.0],[0.0,0.0]])
y = np.array([[4.0],[1.0],[2.0]])
#print(X.shape)
#print(y.shape)


def f(w):
	return (X@w - y).T@(X@w - y)

def fp(w):
	#print(w.shape)
	return 2 * X.T@X@w - 2*X.T@y  

def f_2d(x1, x2):
	return (2*x1 - 4)**2 + (x2 - 1)**2 + 4

x0 = np.array([[1.0], [2.0]])

stepsize = 0.1


x_traces = gd.gd_const_ss(fp, f, x0, stepsize=stepsize)

print(f'stepsize={stepsize}, number of iterations={len(x_traces)-1}')

utils.plot_traces_2d(f_2d, x_traces, f'gd_traces_ss{stepsize}.pdf', stepsize)
#utils.plot(f, x_traces, f'gd_f_ss{stepsize}.pdf', stepsize)