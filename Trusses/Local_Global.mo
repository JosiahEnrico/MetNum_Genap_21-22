function Local_Global
input Real Y[4,4];
input Integer B;
input Integer p1;
input Integer p2;
output Real G[B,B];

algorithm

for i in 1:B loop
 for j in 1:B loop
     G[i,j]:=0;
 end for;
end for;

G[2*p1,2*p1]:=Y[2,2];
G[2*p1-1,2*p1-1]:=Y[1,1];
G[2*p1,2*p1-1]:=Y[2,1];
G[2*p1-1,2*p1]:=Y[1,2];

G[2*p2,2*p2]:=Y[4,4];
G[2*p2-1,2*p2-1]:=Y[3,3];
G[2*p2,2*p2-1]:=Y[4,3];
G[2*p2-1,2*p2]:=Y[3,4];

G[2*p2,2*p1]:=Y[4,2];
G[2*p2-1,2*p1-1]:=Y[3,1];
G[2*p2,2*p1-1]:=Y[4,1];
G[2*p2-1,2*p1]:=Y[3,2];

G[2*p1,2*p2]:=Y[2,4];
G[2*p1-1,2*p2-1]:=Y[1,3];
G[2*p1,2*p2-1]:=Y[2,3];
G[2*p1-1,2*p2]:=Y[1,4];

end Local_Global;
