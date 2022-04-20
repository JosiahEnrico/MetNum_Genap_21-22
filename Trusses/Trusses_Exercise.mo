model Trusses_Exercise

parameter Integer N=6; //Global matrice = 2*points connected
parameter Real A=2.5; //in^2
parameter Real E=10e6; //ln/in^2

Real Sol[N]; //global dispplacement
Real R[N]; //global reaction force
Real SolMat[N,1];
Real XMat[N,1];

//Force Definition
//         fx, fy
Real X[N]={0,   0,
           0,-200,
           0,   0};

//boundary coundition
Integer b1=1;
Integer b2=3;

protected
//truss 1
parameter Real X1=60; //degree between truss
Real l1=48; //in
Real k1=A*E/l1;
Real K1[4,4]; //stiffness matrice
Integer p1a=1;
Integer p1b=2;
Real G1[N,N];

//truss 2
parameter Real X2=120; //degree between truss
Real l2=48; //in
Real k2=A*E/l2;
Real K2[4,4]; //stiffness matrice
Integer p2a=2;
Integer p2b=3;
Real G2[N,N];

//Matrice Generation
Real G[N,N]; //global
Real Ginitial[N,N]; //global


/*
for each truss, please ensure pXa is lower then pXb (X represents truss element number)
*/

algorithm

//creating global matrice
K1:=Stiffness_Matrices(X1);
G1:=k1*Local_Global(K1,N,p1a,p1b);

K2:=Stiffness_Matrices(X2);
G2:=k2*Local_Global(K2,N,p2a,p2b);

G:=G1+G2;
Ginitial:=G;

//implementing boundary condition
for i in 1:N loop
 G[2*b1-1,i]:=0;
 G[2*b1,i]:=0;
 G[2*b2-1,i]:=0;
 G[2*b2,i]:=0;
end for;

G[2*b1-1,2*b1-1]:=1;
G[2*b1,2*b1]:=1;
G[2*b2-1,2*b2-1]:=1;
G[2*b2,2*b2]:=1;

//solving displacement
Sol:=Gauss_Jordan(N,G,X);

//solving reaction force
SolMat:=matrix(Sol);
XMat:=matrix(X);
R:=Reaction_Trusses(N,Ginitial,SolMat,XMat);

end Trusses_Exercise;
