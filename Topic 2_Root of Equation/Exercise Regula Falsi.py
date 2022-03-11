# Defining Function
def f(x):
    return x**3-5*x-9

# Implementing False Position Method
def falsePosition(xa,xb,e,N):
    err = 1
    for step in range(N):
        xt = xa - (xb-xa) * f(xa)/( f(xb) - f(xa) )
        print('Iteration-%d, x2 = %0.6f and err = %0.6f' % (step, xt, err))
        err = abs(1 - xa/xt)
        if f(xa) * f(xt) < 0:
            xb = xt
        else:
            xa = xt

    if err > e:
        print('\nNot Convergent')
    else:
        print('\nRequired root is: %0.8f' % xt)
    return   


# Input Section
xa = input('First Guess: ')
xb = input('Second Guess: ')
e = input('Tolerable Error: ')
N = input('Max Iteration: ')

# Converting input to float
xa = float(xa)
xb = float(xb)
e = float(e)
N = int(N)

#Note: You can combine above two section like this
# x0 = float(input('First Guess: '))
# x1 = float(input('Second Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Max Iteration: '))

# Checking Correctness of initial guess values and false positioning
if f(xa) * f(xb) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    falsePosition(xa,xb,e,N)