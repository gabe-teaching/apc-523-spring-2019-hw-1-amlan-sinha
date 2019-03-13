import numpy as np
import matplotlib.pyplot as plt

def fun_with_square_roots(x,k):

    sqrt_x = np.sqrt(x)

    for i in range(1,k):
        sqrt_x = np.sqrt(sqrt_x)

    x_orig = sqrt_x**2
    for j in range(1,k):
        x_orig = x_orig**2

    return x_orig


k = [49,50,51,52,53,54,55]
x = np.linspace(1.0,10.0,1001)
X = np.zeros((len(k),len(x)))
err = np.zeros((len(k),len(x)))

x_good = np.full((len(k),len(x)),np.nan)

if_plot = 1

tol = 0.01

for i in range(1,len(k)+1):
    X[i-1,] = fun_with_square_roots(x,k[i-1])
    err[i-1,] = np.abs(x-X[i-1,])
    idx = np.array(err[i-1,]<=tol)
    x_good[i-1,idx==True] = x[idx==True]

    if if_plot == 1:

        plt.figure(1)
        plt.subplot(2,4,i)
        plt.plot(x,X[i-1,],'r--')
        plt.plot(x,x,'g')
        plt.plot(x_good[i-1,idx==True],X[i-1,idx==True],'k.')
        plt.title('k = %d' %k[i-1])
        plt.xlabel('original x')
        plt.ylabel('recovered x')

        plt.figure(2)
        plt.subplot(2,4,i)
        plt.plot(x,err[i-1,],'r')
        plt.plot(x_good[i-1,idx==True],err[i-1,idx==True],'k.')
        plt.title('k = %d' %k[i-1])
        plt.xlabel('original x')
        plt.ylabel('error')


if if_plot == 1:
    plt.show()
