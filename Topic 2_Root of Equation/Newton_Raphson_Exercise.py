#Unfinish code exercise for Numerical Method Class
#Written by Josiah Enrico S / M19

import numpy as py

# Defining Function
def f(x): return x**3 - 5*x - 9
# Defining derivative of function
def g(x): return 3*x**2 - 5

def newtonRaphson(xo,tol,N):
    for step in range(N):
        # TODO1 = Complete the blank code below with Newton Raphson Algorithm using for loop
        ...
        ...
        ...
        ...
        ...
        
        print('Step ke-%d, x1 = %0.6f and err = %0.6f' % (step+1, ... , ...))  
    
    # TODO2 = Complete the blank variables below so it will return to 'Not Convergent' if the desired tolerable error is not obtained
    if ... > ...:
        print('\nNot Convergent')
    else:
        print('\nRequired root is: %0.8f' % xt)
    return 

# Input Section
xo = input('Enter Guess: ')
tol = input('Tolerable Error: ')
N = input('Maximum Step: ')

# Converting x0 and e to float and Integer
xo = float(xo)
tol = float(tol)
N = int(N)

#Note: You can combine above three section like this
# x0 = float(input('Enter Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Newton Raphson Method
newtonRaphson(xo,tol,N)
