import numpy as np
import proj_gd
import utils
import matplotlib.pyplot as plt
import matplotlib.patches as patches

X = np.array([[2, 0], [0, 1], [0, 0]])
y = np.array([4,1,2])
r = 1

def f(x):
	return 0.5 * np.linalg.norm(X@x - y)

def fp(x):
	#   START OF YOUR CODE
	return X.T@(X@x - y)
	#	END OF YOUR CODE

def f_2d(x1, x2):
	return 0.5*((2*x1 - 4)**2 + (x2-1)**2 + 4)

def proj_norm1(xy, radius = 1):
	xy_norm1 = np.linalg.norm(xy, ord=1)

	if xy_norm1 <= radius:
		return xy
	
	tempy = np.flip(np.sort(np.abs(xy)))
	mu = (np.cumsum(tempy) - radius)/np.arange(1, len(tempy)+1)
	k = np.where(mu <= tempy)[0][-1]
	return np.sign(xy) * np.maximum(np.abs(xy)-mu[k], 0)



x0 = np.array([0,1.5])
path = "D:/线性优化与凸优化/code_h5/"
stepsize = 0.1

#### Newton
x_traces, y_traces = proj_gd.proj_gd(fp, proj_norm1, x0, stepsize)

diamond = patches.Polygon([(-1, 0), (0, -1), (1, 0), (0, 1)], closed=True)

print("proj_gd")
print('number of iterations:', len(x_traces)-1)
print('solution:', x_traces[-1])
#print('  value:', f_value)

utils.plot_traces_2d(f_2d, x_traces, y_traces, diamond, path+'gd_proj.pdf')
utils.plot(f, x_traces, path+'gd_proj2.pdf')