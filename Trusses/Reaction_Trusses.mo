function Reaction_Trusses

input Integer N;
input Real A[N,N];
input Real B[N,1];
input Real C[N,1];
output Real Sol[N];

protected
Real X[N,1];
Real float_error = 10e-10;

algorithm
X:=A*B-C;

for i in 1:N loop
 if abs(X[i,1]) <= float_error then
   X[i,1] := 0;
 end if;
end for;

for i in 1:N loop
 Sol[i]:=X[i,1];
end for;

end Reaction_Trusses;
