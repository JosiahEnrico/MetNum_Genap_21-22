#Exercise for Numerical Method DTM FTUI
#Written by Numerical Method Assistants


# Defining Function
def f(x):
    return x**3 - 5*x - 9

# Implementing Secant Method
def secant(x0,x1,tol,N):
    for step in range(N):
        # TODO1 = Complete the blank code below with Secant Algorithm using for loop
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
        print('\nRequired root is: %0.8f' % x2)
    return   

# Input Section
x0 = input('Enter First Guess: ')
x1 = input('Enter Second Guess: ')
tol = input('Tolerable Error: ')
N = input('Maximum Step: ')

# Converting x0 and e to float
x0 = float(x0)
x1 = float(x1)
tol = float(tol)

# Converting N to integer
N = int(N)

#Note: You can combine above three section like this
# x0 = float(input('Enter First Guess: '))
# x1 = float(input('Enter Second Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Secant Method
secant(x0,x1,tol,N)
