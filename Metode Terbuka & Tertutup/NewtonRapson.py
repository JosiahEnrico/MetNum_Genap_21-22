import math as m 

print('------Metode Newton Raphson-----')
# Mendefinisikan nilai persamaan f(v) yang didapat
# def = defining a function 
def f(x):
    return x**2 - 2*x + 1

# Mendefinisikan turunan dari f(v) atau f'(v)
def df(x):
    return 2*x - 2

# menginput data untuk dimasukkan ke dalam iterasi
def inputdata():
    # Tipe data integer, float, string, Boolean
    # integer = angka
    # float = bilangan real Ex. 0.1, 1, 2, 3
    # string = "saya rey", "12345", '' 

    Xns = float(input('Estimasi Awal: '))
    t = float(input('Toleransi: '))
    return (Xns, t)

# Fungsi untuk memulai seluruh algoritma Metode Newton Raphson
def NewtonRaphson():
    Xns, t = inputdata()
    # print(Xns, f(Xns), df(Xns))
    for i in range(100):
        # Fungsi range(100) itu iterasi maksimum
        Xp = Xns - f(Xns)/df(Xns)
        # print(Xp, f(Xp), df(Xp))
        if abs(f(Xns)) < t : 
            result = Xns
            print('Akar persamaan =', round(result,4)  )
            print('Iterasi ke - ', i)
            break
        else:
            Xns = Xp

# Memanggil fungsi NewtonRapshon
NewtonRaphson()

# num = 500 # Number
# # Umur saya 500 tahun
# print("Umur saya %s tahun" %num)
# print("umur saya", num, "tahun")