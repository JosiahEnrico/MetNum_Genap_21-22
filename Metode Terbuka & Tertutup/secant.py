import math as m

#Mendfeiniskan Persamaan yang didapatkan dr model matematika
def f(x):
    return m.exp(-x) - x

# Menginput data untuk dimasukan dalam proses iterasi
def inputdata():
    Xns1 = float(input('Estimasi Xns1: '))
    Xns2 = float(input('Estimasi Xns2: '))
    t = float(input('Toleransi : '))
    return (Xns1, Xns2, t)

# Fungsi untuk memulai seluruh proses Metode Secant
def Secant(): 
    Xns1, Xns2, t = inputdata()
    for i in range(100):
        i = i + 1
        Xns = Xns1 - (Xns2-Xns1)*f(Xns1)/( f(Xns2) - f(Xns1) ) 
        print(Xns)
        if abs(f(Xns)) > t : 
            Xns1 = Xns2
            Xns2 = Xns
        else:
            break            
    print('akar peramaan =', Xns )
    print('Iterasi ke - ', i)

# Memanggil Fungsi Secant
Secant()
