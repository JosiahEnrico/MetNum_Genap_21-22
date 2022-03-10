# Numpy, math, matplotlib
# Import Library

import math as m

# Mendefiniskan nilai persamaan f(x) yang didapat
def f(x):
    return x**2 - 2*x + 1

#Equations
# + - / *, Kuadrat = **, 2x = 2*x, x^2 = x**2

# Mendefinisikan Turunanya
def df(x):
    return 2*x - 2


# Mendifiniskan Data awal, input, toleransi 
def inputdata():
    # Tipe Data: Integer, string, float, boolean
    # Integer : 1,2,3,4,5
    # String : "Saya Rey", "1223445",''
    # float : bilangan real , 0.1,0.2,133
    # Boolean : True & False 
    
    # Data awal
    x0 = float(input('Estimasi Awal x0: '))
    tol = float(input("Toleransi: "))
    return (x0, tol)

# Fungsi untuk memulai algoritma dari Newton Raphson
def NewtonRaphson():
    # Mengambil Data awal dari Function inputdata()
    x0, tol = inputdata()
    #looping : for loop, while loop, Do While
    # Kita akan melakukan looping, dari data ke-i sampai maximal range itu 100 (iterasi maksimal)
    for i in range(100):
        # i adalah iterasi ke-i
        # Apa yang mau di iterasi? 
        xp = x0 - f(x0)/df(x0)
        # Kondisi kalo konvergen
        if abs(f(xp)) < tol:
            result = xp
            print("Akar Persamaan =", result)
            print("Pada Iterasi ke-", i)
            #Stop Looping dengan break
            break
        # Kalo ga konvergen? iterasi lanjut
        else:
            x0 = xp

#Panggil function NewtonRaphson()
NewtonRaphson()