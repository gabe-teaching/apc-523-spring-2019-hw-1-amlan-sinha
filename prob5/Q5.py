import numpy as np

m = np.linspace(0,20,21)
e = np.zeros(21)
n = 10**m

k = 13

print('         n     Current estimate for epsilon')
e[0] = (1+(1/n[0]))**n[0]
print('{:>10.1e}{:>33.11f}'.format(1,round(e[0],k)))
for i in range(1,len(m)):
    e[i] = (1+(1/n[i]))**n[i]
    print('{:>10.1e}{:>33.11f}'.format(n[i],round(e[i],k)))
    if round(e[i],k)==round(e[i-1],k):
        index = i+1
        print('n_stop = %d' %index)
        print('current estimate for epsilon = %d' %round(e[i],k))
        break
