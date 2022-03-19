import math as m

print('------Metode Regula Falsi-----')
# Persamaan Volume mencari V
def f(x):
    return m.exp(-x)-x

# Menginput data range dan toleransi
def inputdata():
    a = float(input("Range a : "))
    b = float(input("Range b : "))
    p = float(input("Toleransi : "))
    return (a,b,p)

# Mengecek Algoritma ke 4 pada Metode Regula Falsi
def checkAB(a,b):
    if(f(a)*f(b)<0):
        return True
    else:
        return False

# Menghitung Nilai Tengah Xns
def updateData(a,b):
    c = (a*f(b)-b*f(a))/(f(b)-f(a))
    if(f(a)*f(c)<0):
        # Batas Bawah432q       2q3W
        b = c 

    else :
        a = c
    return (a,b)

# Looping Algoritma & iterasi untuk mencari nilai akhir
def process(a,b,p):
    i = 0
    while(abs(f(a))>p and abs(f(b))>p):
        i = i +1
        a,b = updateData(a,b)
    print('Hasil akhir pada iterasi ke - ', i)
    if(abs(f(a))>abs(f(b))):
        return b
    else:
        return a
    return (a,b)
   
# Initial Condition dari Algoritma Awal
def main():
    a,b,p = inputdata()
    if(checkAB(a,b)):
        resultX = process(a,b,p)
        #resultY = g(resultX)
        print ("Akar persamaan = ",resultX )
    else:
        print ("Data tidak sesuai & tidak bisa dilanjutkan")
        
# Memanggil fungsi main() utnuk menjalankan algoritma
main()
