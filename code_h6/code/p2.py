import numpy as np
import LP

## parameters of the standard form dual LP 
c =  np.array([[-6.0], [-8.0], [0.0], [0.0]])
A =  np.array([[-1.0, 1.0, 1.0, 0.0],[-1.0, -2.0, 0.0, 1.0]])
b =  np.array([[-1.0], [-3.0]])

#mu0 = np.array([4,1,2,3], dtype=float)
mu0 = np.array([[4.0], [1.0], [2.0], [3.0]])

mu_traces = LP.barrier(-c, A, b, mu0)

print('')
for k,mu in enumerate(mu_traces):
	print('iteration %d: %s' % (k, mu))
print('dual optimal value:', c.T@mu_traces[-1])
