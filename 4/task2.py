x1, y1, z1 = map(int, input().split(',')) 
x2, y2, z2 = map(int, input().split(','))
x3, y3, z3 = map(int, input().split(',')) 

xmax,ymax,zmax=max(x1,x2,x3), max(y1,y2,y3), max(z1,z2,z3)
xmin,ymin,zmin=min(x1,x2,x3),min(y1,y2,y3),min(z1,z2,z3)
s=(xmax-xmin)*(ymax-ymin)*(zmax-zmin)
print(s)
