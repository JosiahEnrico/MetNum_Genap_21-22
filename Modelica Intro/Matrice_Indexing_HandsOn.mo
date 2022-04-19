model Matrice_Indexing_HandsOn

parameter Real A[2,5] = [ 1, 9, 0, 6, 3;
                          5, 6, 2, 8, 6];
                        
Real B[6,2];

equation

for i in 1:5 loop
  for j in 1:2 loop
    B[i,j] = A [3-j, i]; 
  end for;
end for;

B[6,1] = A[2,1];
B[6,2] = A[1,1];

/*
[ 5, 1;
  6, 9;
  2, 0;
  8, 6;
  6, 3;
  5, 1];
*/

end Matrice_Indexing_HandsOn;
