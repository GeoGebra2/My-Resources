import numpy as np
import newton
import utils
import math

A = np.array([[1,1,1]])
b = np.array([[1]])

def f_2d(x1, x2, x3):
    return math.exp(2*x1) + math.exp(x2) + math.exp(x3)

def f(x):
    return f_2d(x[0], x[1], x[2])

def fp(x):
    return np.array([[2*math.exp(2*x[0])], [math.exp(x[1])], [math.exp(x[2])]])

def fpp(x):
    return np.array([[4*math.exp(2* x[0]), 0, 0], [0, math.exp(x[1]), 0], [0, 0, math.exp(x[2])]])

x0 = np.array([[0],[1],[0]])
x_traces = newton.newton_eq(f,fp,fpp,x0,A,b)


print('number of iterations:', len(x_traces)-1)
print('solution:', x_traces[-1])

path = "D:/线性优化与凸优化/code_h5/"
#utils.plot_traces_2d(f_2d, x_traces, path+f'newton.pdf')
#utils.plot(f, x_traces, path+f'newton2.pdf')
