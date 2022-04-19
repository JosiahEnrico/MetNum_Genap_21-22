model Library_Function

Real A[3,3] = [1,2,3;
               3,4,5;
               2,1,4];
Real b[3] = {10,22,12};
Real x[3];
Real y;
  
algorithm

x := Modelica.Math.Matrices.solve(A,b);  // x = [3,2,1]
y := Modelica.Math.Vectors.length(b); // y = 26.9815

end Library_Function;
