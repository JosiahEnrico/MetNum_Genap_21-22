model Intro_2
parameter Real R = 1; //Radius silinder
parameter Real A=0.1; //Luas outlet


constant Real pi = Modelica.Constants.pi;
constant Real g = 9.81;

Real u; //kecepatan fluida outlet
Real V; //Volume fluida dalam silinder
Real h; //Tinggi fluida dalam silinder

function VolumeSilinder

input Real h_silinder;
input Real R_silinder;
output Real V_silinder;

algorithm
V_silinder := pi*(R_silinder^2)*h_silinder;

end Intro_2;
