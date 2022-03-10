import numpy as np

#1. Define matrix
# Matrix segitiga atas

A= np.array ([[1,2,3], [2,3,4], [3,4,4]], float)
B= np.array ([18,25,50], float)
n= len(A)

#2. Eliminasi gauss

for k in range(0,n-1): #Looping Kolom
    for i in range(k+1,n): #looping  Basris
        if A[i,k] != 0: #Iterasi Nilai tidak sama dengan 0
            ratio = A[i,k]/A[k,k]
            A[i,k:n] = A[i,k:n]-(A[k,k:n]*ratio)
            B[i]=B[i]-(B[k]*ratio)

print('matrix A : ', '\n', A)

#3. Back substitution

x = np.zeros(n,float)
print(x)

for m in range(n-1, -1, -1):
    x[m]=(B[m]-np.dot(A[m,m+1:n], x[m+1:n]))/A[m,m]
    print('Nilai X', m+1, '=', x[m])
