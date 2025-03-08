import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0.132,0.135,0.136,0.159,0.168,0.172,0.220,0.225,0.291])
ypoints = np.array([0.930,0.907,0.900,0.775,0.722,0.716,0.552,0.545,0.424])
xpoints2 = np.array([0.220,0.168,0.135,0.132,0.136,0.159,0.172,0.225,0.291])
ypoints2 = np.array([1,2,3,3.7,4,4.7,5,6,7])
plt.plot(ypoints2,xpoints2, marker = 'o')
plt.ylabel('I/A')  
plt.xlabel('C/'+ str(chr(956)) + 'F')
plt.show()
