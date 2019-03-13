import numpy as np

N = 32
y_n = 0

for n in range(N,20,-1):
    y_n = (np.exp(1)-y_n)/n

print('y_20 = ', y_n)
