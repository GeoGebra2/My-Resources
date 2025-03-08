import numpy as np
import LP
import matplotlib.pyplot as plt

## parameters of the standard form LP 

c =  np.array([[-1.0], [-3.0], [0.0], [0.0]])
A =  np.array([[1.0, 1.0, 1.0 ,0.0],[-1.0, 2.0, 0.0, 1.0]])
b =  np.array([[6.0], [8.0]])

x0 =  np.array([[3.0], [1.0], [2.0], [9.0]])
#x0 = np.array([[1.63307563],[3.90402064],[0.46290373],[1.82503435]])
#print(np.log(x0))
x_traces = LP.barrier(c, A, b, x0)

print('')
for k,x in enumerate(x_traces):
	print('iteration %d: %s' % (k, x))
print('optimal value:', c.T@x_traces[-1])

### visualization
x12 = [x[0:2] for x in x_traces]
fig = plt.figure()
plt.plot([0,0, 4/3, 6,0], [0,4, 14/3, 0, 0], color='blue', linewidth=3)
line, = plt.plot(*zip(*x12), color='red', linewidth=3,  label='barrier method')
plt.scatter(*zip(*x12), color='red', marker='o', s=50)
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend(handles=[line], fontsize=20)
plt.tight_layout()
fig.savefig('D:\线性优化与凸优化\code_h6 - 副本\code\p1.png')


