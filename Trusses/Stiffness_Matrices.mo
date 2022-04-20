function Stiffness_Matrices
input Real A;
output Real X[4,4];

protected
Real Y;
Real float_error = 10e-10;
final constant Real pi=2*Modelica.Math.asin(1.0);

algorithm

Y:=A/180*pi;
    
X:=[(Modelica.Math.cos(Y))^2,Modelica.Math.cos(Y)*Modelica.Math.sin(Y),-(Modelica.Math.cos(Y))^2,-Modelica.Math.cos(Y)*Modelica.Math.sin(Y);

Modelica.Math.cos(Y)*Modelica.Math.sin(Y),(Modelica.Math.sin(Y))^2,-Modelica.Math.cos(Y)*Modelica.Math.sin(Y),-(Modelica.Math.sin(Y))^2;

-(Modelica.Math.cos(Y))^2,-Modelica.Math.cos(Y)*Modelica.Math.sin(Y),(Modelica.Math.cos(Y))^2,Modelica.Math.cos(Y)*Modelica.Math.sin(Y);

-Modelica.Math.cos(Y)*Modelica.Math.sin(Y),-(Modelica.Math.sin(Y))^2,Modelica.Math.cos(Y)*Modelica.Math.sin(Y),(Modelica.Math.sin(Y))^2];

for i in 1:4 loop
 for j in 1:4 loop
   if abs(X[i,j]) <= float_error then
     X[i,j] := 0;
   end if;
 end for;
end for;

end Stiffness_Matrices;
