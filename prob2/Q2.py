import numpy as np
import copy

def my_round_to_n(x,n):
    s = '%.'+str(n)+'g'
    x = float(s % x)
    return x

def my_factorial(n):
    n = my_round_to_n(float(n),5)
    if n == 1:
        x = n
        return my_round_to_n(x,5)
    else:
        x = n*my_factorial(n-1)
        return my_round_to_n(x,5)

def my_sum(x):
    sum_x = 0
    for i in range(0,len(x)):
        sum_x = my_round_to_n(sum_x,5)+my_round_to_n(x[i],5)
    return  my_round_to_n(sum_x,5)

# Constants
x = 5.5
n = 31

################################################################################
# part a
# first term
sum_a = 0.0
num_a = 1.0
n_factorial_a = float(1.0)
term_a = np.empty(n)
term_a[0] = my_round_to_n(num_a/n_factorial_a,5)
sum_a = my_round_to_n(sum_a+term_a[0],5)

# n terms
print('Part A')
print('    n            Series Sum')
print('{:>5d}{:>25.10f}'.format(0,sum_a))
for i in range(1,n):
    index = i
    num_a = num_a*x
    num_a = my_round_to_n(num_a,5)
    n_factorial_a = my_factorial(i)
    n_factorial_a = my_round_to_n(n_factorial_a,5)
    term_a[i] = my_round_to_n(num_a/n_factorial_a,5)
    sum_a = my_round_to_n(sum_a+term_a[i],5)
    print('{:>5d}{:>25.10f}'.format(index,sum_a))

################################################################################
# part b
# first term
sum_b = np.empty(n)
sum_b[0] = 0
num_b = 1
n_factorial_b = float(1)
term_b = np.empty(n)
term_b[0] = num_b/n_factorial_b
sum_b[0] = sum_b[0]+term_b[0]

# n terms (until they converge)
print('Part B')
print('    n     Series Sum')
print('{:>5d}{:>25.10f}'.format(0,sum_b[0]))
for i in range(1,n):
    index = i
    num_b = num_b*x
    num_b = my_round_to_n(num_b,5)
    n_factorial_b = my_factorial(i)
    n_factorial_b = my_round_to_n(n_factorial_b,5)
    term_b[i] = my_round_to_n(num_b/n_factorial_b,5)
    prev_sum = sum_b[i-1]
    sum_b[i] = my_round_to_n(sum_b[i-1]+term_b[i],5)
    curr_sum = sum_b[i]
    print('{:>5d}{:>25.10f}'.format(index,sum_b[i]))
    if (curr_sum-prev_sum)==0:
        convergence = 1
        print('k = ', index)
        print('curr_sum =',curr_sum)
        break

################################################################################
# part c
sum_c = np.empty(n)
term_c = copy.copy(term_a)
#term_c = term_c[::-1]
sum_c[0] = 0
sum_c[0] = sum_c[0]+term_c[0]

print('Part C')
print('    n     Series Sum')
print('{:>5d}{:>25.10f}'.format(0,sum_c[0]))
# sum from right to left
for i in range(1,n):
    index = i
    prev_sum = sum_c[i-1]
    term_c_inv = term_c[0:i+1][::-1]
    #sum_c[i] = my_round_to_n(my_sum(term_c_inv),5)
    sum_c[i] = my_round_to_n(sum_c[i-1]+term_c_inv[0],5)
    curr_sum = sum_c[i]
    print('{:>5d}{:>25.10f}'.format(index,sum_c[i]))
    if (curr_sum-prev_sum)==0:
        print('k = ', index)
        print('curr_sum =',curr_sum)
        break

################################################################################
# part d.i.
term_d1 = copy.copy(term_a)
term_d1[1::2] = -term_d1[1::2]
sum_d1 = np.empty(n)
sum_d1[0] = 0
sum_d1[0] = sum_d1[0]+term_d1[0]

print('Part D.i.')
print('    n     Series Sum')
print('{:>5d}{:>25.10f}'.format(0,sum_d1[0]))
# sum from left to right
for i in range(1,n):
    index = i
    prev_sum = sum_d1[i-1]
    sum_d1[i] = my_round_to_n(sum_d1[i-1]+term_d1[i],5)
    curr_sum = sum_d1[i]
    print('{:>5d}{:>25.10f}'.format(index,sum_d1[i]))
    if (curr_sum-prev_sum)==0:
        print('k = ', index)
        print('curr_sum =',curr_sum)
        break
print('error = ',(np.abs(curr_sum-np.exp(-5.5))*100)/np.exp(-5.5),'%')

################################################################################
# part d.ii.
term_d2 = copy.copy(term_a)
term_d2[1::2] = -term_d2[1::2]
#term_d2 = term_d2[::-1]
sum_d2 = np.empty(n)
sum_d2[0] = 0
sum_d2[0] = sum_d2[0]+term_d2[0]

print('Part D.ii.')
print('    n     Series Sum')
print('{:>5d}{:>25.10f}'.format(0,sum_d2[0]))
# sum from right to left
for i in range(1,n):
    index = i
    prev_sum = sum_d2[i-1]

    term_d2_inv = term_d2[0:i+1][::-1]
    #sum_c[i] = my_round_to_n(my_sum(term_c_inv),5)
    sum_d2[i] = my_round_to_n(sum_d2[i-1]+term_d2_inv[0],5)
    curr_sum = sum_d2[i]

    curr_sum = sum_d2[i]
    print('{:>5d}{:>25.10f}'.format(index,sum_d2[i]))
    if (curr_sum-prev_sum)==0:
        print('k = ', index)
        print('curr_sum =',curr_sum)
        break
print('error = ',(np.abs(curr_sum-np.exp(-5.5))*100)/np.exp(-5.5),'%')

################################################################################
# part d.iii.
term_d3 = copy.copy(term_a)
term_d3[1::2] = -term_d3[1::2]
sum_d3 = np.empty(n)
sum_d3[0] = 0
sum_d3[0] = my_round_to_n(my_round_to_n(sum_d3[0],5)+my_round_to_n(term_d3[0],5),5)

print('Part D.iii.')
print('    n     Series Sum')
print('{:>5d}{:>25.10f}'.format(0,sum_d3[0]))
# sum positive terms from left to right and negative terms from left to right
for i in range(1,n):
    index = i
    prev_sum = sum_d3[i-1]
    int_term_d3 = term_d3[0:i+1]
    term_d3_pos = int_term_d3[int_term_d3>0]
    #term_d3_pos = np.append(term_d3[0],term_d3_pos)
    term_d3_neg = int_term_d3[int_term_d3<0]

    sum_d3[i] = my_round_to_n(my_sum(term_d3_pos)+my_sum(term_d3_neg),5)

    curr_sum = sum_d3[i]
    print('{:>5d}{:>25.10f}'.format(index,sum_d3[i]))
    if (curr_sum-prev_sum)==0:
        print('k = ', index)
        print('curr_sum =',curr_sum)
        break
print('error = ',(np.abs(curr_sum-np.exp(-5.5))*100)/np.exp(-5.5),'%')

################################################################################
# part d.iv.
term_d4 = copy.copy(term_a)
term_d4[1::2] = -term_d4[1::2]
sum_d4 = np.empty(n)
sum_d4[0] = 0
sum_d4[0] = sum_d4[0]+term_d4[0]

print('Part D.iv.')
print('    n     Series Sum')
print('{:>5d}{:>25.10f}'.format(0,sum_d4[0]))
# sum positive terms from left to right and negative terms from right to left
for i in range(1,n):
    index = i
    prev_sum = sum_d4[i-1]
    int_term_d4 = term_d4[0:i+1]
    term_d4_pos = int_term_d4[int_term_d4>0]
    #term_d3_pos = np.append(term_d3[0],term_d3_pos)
    term_d4_neg = int_term_d4[int_term_d4<0]
    term_d4_neg = term_d4_neg[::-1]
    sum_d4[i] = my_round_to_n(my_sum(term_d4_pos)+my_sum(term_d4_neg),5)
    curr_sum = sum_d4[i]
    print('{:>5d}{:>25.10f}'.format(index,sum_d4[i]))
    if (curr_sum-prev_sum)==0:
        print('k = ', index)
        print('curr_sum =',curr_sum)
        break
print('error = ',(np.abs(curr_sum-np.exp(-5.5))*100)/np.exp(-5.5),'%')

################################################################################
# part e
sum_e = np.empty(n)
sum_e[0] = 0
num_e = 1
n_factorial_e = float(1)
term_e = np.empty(n)
term_e[0] = num_e/n_factorial_e
sum_e[0] = sum_e[0]+term_e[0]

# n terms (until they converge)
print('Part E')
print('    n     Series Sum')
print('{:>5d}{:>25.10f}'.format(0,sum_e[0]))
for i in range(1,n):
    index = i
    num_e = num_e*x
    num_e = my_round_to_n(num_e,5)
    n_factorial_e = my_factorial(i)
    n_factorial_e = my_round_to_n(n_factorial_e,5)
    term_e[i] = my_round_to_n(num_e/n_factorial_e,5)
    prev_sum = 1/sum_e[i-1]
    sum_e[i] = my_round_to_n(sum_e[i-1]+term_e[i],5)
    curr_sum = 1/sum_e[i]
    print('{:>5d}{:>25.10f}'.format(index,curr_sum))
    if (curr_sum-prev_sum)==0:
        convergence = 1
        print('k = ', index)
        print('curr_sum =',curr_sum)
        break
print('error = ',(np.abs(curr_sum-np.exp(-5.5))*100)/np.exp(-5.5),'%')
