import math as m

print('------Metode Bisection-----')
# Definiskan fungsi f(x) yang didapat dari permodelan
def f(x):
    return m.exp(-x)-x

# Menginput data range dan toleransi
def inputdata():
    a = float(input("Range a : "))
    b = float(input("Range b : "))
    p = float(input("Toleransi : "))
    return (a,b,p)

# Mengecek Algoritma ke 4 pada Metode Bisection
def checkAB(a,b):
    if(f(a)*f(b)<0):
        return True
    else:
        return False

# Menghitung Nilai Xns dengan Metode Bisection
def updateData(a,b):
    # C = Xns (Nilai Tengah)
    c= (a+b)/2
    if(f(a)*f(c)<0):
        b = c 
    else :
        a = c
    return (a,b)

# Looping Algoritma & Iterasi untuk mencari nilai akhir
def process(a,b,p):
    # Iterasi dimulai dari 0
    i = 0
    while(abs(f(a))>p or abs(f(b))>p):
        i = i + 1
        a,b = updateData(a,b)
    print('Hasil pada Iterasi ke - ', i)

    #Dicari yang jarak intervalnya lebih sedikit / paling mendekati akar
    if(abs(f(a))>abs(f(b))):
        return b
    else:
        return a
    
   
# Initial Condition dari Algoritma Awal
def main():
    a,b,p = inputdata()
    if(checkAB(a,b)):
        result = process(a,b,p)
        print ("Akar persamaan ",round(result,4))
    else:
        print ("Data tidak sesuai tidak bisa dilanjutkan")

# Memanggil fungsi main() utnuk menjalankan algoritma
main()
