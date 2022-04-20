function Gauss_Jordan

input Integer N;
input Real A[N,N];
input Real B[N];
output Real X[N];

protected
Real float_error = 10e-10;

algorithm
X:=Modelica.Math.Matrices.solve(A,B);

for i in 1:N loop
 if abs(X[i]) <= float_error then
   X[i] := 0;
 end if;
end for;

end Gauss_Jordan;
