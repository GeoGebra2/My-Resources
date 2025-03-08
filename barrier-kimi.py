import numpy as np
from scipy.optimize import minimize

# 定义LP问题的目标函数
def objective(x, c, A, b, t):
    # f(x) = c^T x
    return c @ x + 1 / t * sum(np.log(-b @ x + b))

# 定义LP问题的约束条件
def constraints(x, A, b):
    # Ax = b
    return A @ x - b

# LP问题的参数
#c = np.array([-1, -3])  # 目标函数系数
#A = np.array([[1, 1], [-1, 2]])  # 约束条件系数
#b = np.array([6, 8])  # 约束条件右侧值
#x0 = np.array([0, 0])  # 初始点
c =  np.array([-1.0, -3.0, 0.0, 0.0])
A =  np.array([[1.0, 1.0, 1.0 ,0.0],[-1.0, 2.0, 0.0, 1.0]])
b =  np.array([6.0, 8.0])

x0 =  np.array([3.0, 1.0, 3.0, 6.5])

# Barrier方法参数
t = 1  # barrier参数，控制近似精度
rho = 10  # 参数更新比例
max_iter = 100  # 最大迭代次数

# 初始参数
x = x0
for k in range(max_iter):
    # 定义优化问题
    prob = {
        'fun': lambda x: objective(x, c, A, b, t),
        'x0': x,
        'constraints': ({'type': 'eq', 'fun': lambda x: constraints(x, A, b)}),
        'bounds': [(0, None), (0, None)]  # x1, x2 >= 0
    }
    
    # 使用minimize函数进行优化
    result = minimize(**prob)
    
    # 检查是否达到最大迭代次数或者是否找到解
    if result.success or k == max_iter - 1:
        print(f"Optimal solution: {result.x}")
        print(f"Optimal value: {-result.fun}")  # 取负号是因为目标函数是最小化
        break
    
    # 更新参数t
    t *= rho
    x = result.x

# 运行barrier算法
if __name__ == "__main__":
    t = 1
    for _ in range(10):  # 这里我们只迭代10次作为示例
        res = minimize(
            fun=lambda x: objective(x, c, A, b, t),
            x0=x0,
            method='SLSQP',
            constraints=[{'type': 'eq', 'fun': lambda x: constraints(x, A, b)}],
            bounds=[(0, None), (0, None)]
        )
        if res.success:
            print(f"Iteration {_+1}, x: {res.x}, f(x): {-res.fun}")
            t *= 10  # 增加t的值
            x0 = res.x  # 使用上一次的结果作为下一次的起点
        else:
            print("Optimization failed.")
            break