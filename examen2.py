def mitadFin(cad,n):
	s=" "
	tam=len(cad)
	if tam%2==0:
		string=cad[tam//2: ]
	else:
		string=cad[tam//2+1: ]
	for i in range(n):
		s+=string
	return s
def ingresar(M,f,c):
	for i in range(f):
		for j in range(c):
			M[i][j]=int(input("Valor?: "))
	return M
def Mostrar(M,f,c):
	for i in range(f):
		for j in range(c):
			print(M[i][j],end=" ")
		print ()
		
def mostrar(v,c):
	for i in range(c):
		print(v[i])
def difMayMenCol(M,f,c):
	v=[0]*c
	for i in range(c):
		may=M[0][i]
		men=M[0][i]
		for j in range(1,f):
			if M[j][i]>may:
				may=M[j][i]
			if M[j][i]<men:
				men=M[j][i]
		v[i]=may-men
	mostrar(v,c)

def difDiagonales(M,n):
	v=[0]*n
	may=[0][0]
	men=[0][n-1]
	for i in range(1,n):
		if M[i][j]>may:
			may=M[i][i]
		if M[i][n-i-1]<men:
			men=M[i][n-1-i]
		v[i]=may-men
	mostrar(v,c)

def menor(M,i,c):
	men=[i][0]
	for j in range (1,c):
		if M[i][j]<men:
			men=M[i][j]
	return men
def mayor(M,j,f):
	may=[0][j]
	for i in range (1,f):
		if M[i][j]>may:
			may=M[i][j]
	return may

def puntoSilla(M,f,c):
	
	
	for i in range(f):
		for j in range(c):
			val=M[i][j]
			if val==menor(M,i,c)and val==mayor(M,j,f):
				print ("( ",i,",",j,")")
	
			
	
'''cad=input("cadena?")
n=int(input("N?"))
print(mitadFin(cad,n))'''

M=[]
f=int(input("filas?: "))
c=int(input("columnas?: "))
for i in range(f):
	M.append([0]*c)
ingresar(M,f,c)
Mostrar(M,f,c)
difMayMenCol(M,f,c)
