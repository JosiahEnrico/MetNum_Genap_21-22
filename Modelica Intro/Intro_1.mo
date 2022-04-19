model Intro_1
parameter Real R = 1; //Radius silinder
parameter Real A=0.1; //Luas outlet


constant Real pi = Modelica.Constants.pi;
constant Real g = 9.81;

Real u; //kecepatan fluida outlet
Real V; //Volume fluida dalam silinder
Real h; //Tinggi fluida dalam silinder

initial equation
h = 2; //kondisi h mula-mula

equation
u = (2*g*h)^0.5; // torriceli's law
V = pi*(R^2)*h; //Volume fluida dalam silinder
der(V) = -A*u; // debit fluida outlet

end Intro_1;
