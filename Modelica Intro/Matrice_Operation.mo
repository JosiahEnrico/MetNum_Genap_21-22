model Matrice_Operation
  
parameter Real A[3,3]=[  2,   3,   4; 
                         2,   3,   4;    
                         2,   1,   4];
                                         
parameter Real B[3,3]=[  2,   3,   4; 
                         2,   3,   4;    
                         1,   1,   4];
                         
parameter Real C[2,3]=[  2,   3,   4;    
                         1,   1,   4];

parameter Real D[3,2]=[  2,   3; 
                         2,   4;    
                         1,   4];
        
Real Ma[3,3];
Real Mat[3,3];
Real Matr[3,3];
Real Matri[2,2];

equation

Ma = A+B;
/*
[ 4, 6, 8;
  4, 6, 8;
  3, 2, 8];
*/
Mat = A-B;
/*
[ 0, 0, 0;
  0, 0, 0;
  1, 0, 0];
*/
Matr = A.*A;
/*
[ 4, 9, 16;
  4, 9, 16;
  4, 9, 16];
*/

Matri = C*D;
/*
[ 14, 34;
   8, 23];
*/

end Matrice_Operation;
