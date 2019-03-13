import numpy as np
from scipy import optimize
import copy

from sympy import *

k = np.linspace(1,20,20)

# part a
wa = np.poly1d(k,True)
wa_coeffs = wa.c
print('Ans a. In descending powers of x, the coefficients are:')
print(*wa_coeffs, sep = ",")
print('\n')

# part b
wb = copy.copy(wa)
wb_coeffs = wa_coeffs.copy()

roots_Nb = optimize.newton(wb,21)

roots_Pb = wb.r
roots_Pb = roots_Pb[::-1]

err_Nb = np.abs(roots_Nb-k[-1])
err_Pb = np.abs(roots_Pb[-1]-k[-1])

print('Ans b.i. Error with Newton-Raphson:',err_Nb)
print('Ans b.ii. Error with the built-in polynomial roots finding function:',err_Pb)
print('\n')

# part c
delta = [0,10**-8,10**-6,10**-4,10**-2]
err_Pc = np.zeros(len(delta))
err_Nc = np.zeros(len(delta))

wc_coeffs = wa_coeffs.copy()

print('Ans c.')
print('     delta     |Newton-Real|    |NumPolyRoot-Real|')
for i in range(len(delta)):

    wc_coeffs[0] = wa_coeffs[0]+delta[i]
    wc = np.poly1d(wc_coeffs)

    roots_Nc = optimize.newton(wc,21,maxiter=100)

    roots_Pc = wc.r
    roots_Pc = roots_Pc[::-1]

    err_Nc[i] = np.abs(roots_Nc-k[-1])
    err_Pc[i] = np.abs(roots_Pc[-1]-k[-1])

    print('{:>10.1e}{:>18.12f}{:>22.12f}'.format(delta[i],err_Nc[i],err_Pc[i]))
    #print('{:>10.1e}{:>18.12f}{:>22.12f}'.format(delta[i],roots_Nc,roots_Pc[-1]))

print('\n')

# part d
wd_coeffs = wa_coeffs.copy()
wd_coeffs[1] = wa_coeffs[1]-2**-23
wd = np.poly1d(wd_coeffs)

roots_Pd = wd.r
roots_Pd = roots_Pd[::-1]

err_Pd = [roots_Pd[15:17]-k[15:17]]

print('Ans d.i.  Error with the built-in polynomial roots finding function (x = 16):',err_Pd)
print('Ans d.ii. Error with the built-in polynomial roots finding function (x = 17):',err_Pd)
print('\n')

p_coeffs = copy.copy(wa_coeffs)
p = np.poly1d(p_coeffs)
dp = np.poly1d.deriv(p)
p_roots = p.r

p_roots = p_roots[::-1]
p_coeffs = p_coeffs[::-1]

cond = np.zeros(len(p))

print('     Roots         Condition Number')
for i in range(0,len(p_roots)):
    for j in range(0,len(p_coeffs)-1):
        cond[i] = cond[i]+abs((p_coeffs[j]*p_roots[i]**(j-1))/dp(p_roots[i]))
    print('{:>10.5f}{:>25.5e}'.format(p_roots[i],cond[i]))
