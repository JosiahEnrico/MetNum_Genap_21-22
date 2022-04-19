model Matrix_Indexing

parameter Real A[3,3]=[  2,   3,   4; 
                         2,   3,   4;    
                         2,   1,   4];

Real Point;
Real Array1[3];
Real Array2[3];
Real Matrix[2,2];

equation

Point = A[3,2]; // Point = 1

for i in 1:3 loop
  Array1[i] = A[i,3]; // [4,4,4]
end for;

Array2 = A[2,:]; // [2,3,4]

for i in 1:2 loop
  for j in 1:2 loop
    Matrix[i,j] = A[i+1,j+1]; // [3,4 ; 1,4]
  end for;
end for;

end Matrix_Indexing;
