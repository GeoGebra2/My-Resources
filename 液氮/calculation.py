import scipy.integrate as integrate
import numpy as np
result = integrate.quad(lambda x: x**3 / (np.exp(x) - 1), 0, 4.39744)
print(result)
