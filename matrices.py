def ingresar (M,f,c):
    for i in range(f):
        for j in range(c):
            M[i][j]=int(input("Valor?: "))
def mostrar(M,f,c):
     for i in range(f):
        for j in range(c):
            print (M[i][j], end=" ")
        print()
def sumar(M,f,c):
    s=0
    for i in range(f):
        for j in range(c):
            s+=M[i][j]
    return s
def sumaParcial(M,f,c):
    
    for i in range(f):
        s=0
        for j in range(c):
            s+=M[i][j]
        print("La suma de la fila",i, "es: ", s)
def sumaDiagonal(M,f,c):
    if f==c:
      s=0
      for i in range(f):
       
        for j in range(c):
            if i==j:
                s+=M[i][j]
            
      print ("La suma de la diagonal de la  matriz es :",s)
    else:
        print("Dimensiones incorrectas")

def sumaDSecundaria(M,f,c):
    if f==c:
      s=0
      temp=c-1
      for i in range(f):
       
        for j in range(c):
            if j==temp:
                s+=M[i][j]
                temp-=1
            
      print ("La suma de la diagonal secuandria de la  matriz es :",s)
    else:
        print("Dimensiones incorrectas")

def contornoM(M,f,c):
	for i in range(f):
		for j in range(c):
			if i==0 or i==f-1 or j==0 or j==c-1:
				print(M[i][j],end="\t")
			else:
				print(" ",end="\t")
		print()
      
def letraN(M,n):
	for i in range(n):
		for j in range(n):
			if i==j or j==0 or j==n-1:
				print(M[i][j],end="\t")
			else:
				print(" ",end="\t")
		print()   
    
def sumDS(M,n):
	s=0
	j=n-1
	for i in range(n):
		s+=M[i][j]
		j-=1
	return s
def sumaDs(M,n):
	s=0
	for i in range(n):
		s+=M[i][n-i-1]
	return s
	
def sumar(M,N,f,c,s):
	for i in range(f):
		for j in range(c):
			s[i][j]=M[i][j]+N[i][j]

M=[]
N=[]
s=[]
f=int(input("filas?: "))
c=int(input("columnas?: "))
for i in range(f):
    M.append([0]*c)
    N.append([0]*c)
    s.append([0]*c)
ingresar (M,f,c)
mostrar(M,f,c)
#3
print ("La suma de la matriz es :",sumar(M,f,c))
#4
sumaParcial(M,f,c)
#5
sumaDiagonal(M,f,c)
#6
sumaDSecundaria(M,f,c)
#7
contornoM(M,f,c)
