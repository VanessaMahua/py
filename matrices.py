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
    
      s=0
      temp=c-1
      for i in range(f):
       
        for j in range(c):
            if j==temp or i==j :
                if i==0:
                    print(M[i][j],end=" ")
                temp-=1
                print(end=", ")
            else:
                print(M[i][j])
        
        print()  
      
    
    

M=[]
f=int(input("filas?: "))
c=int(input("columnas?: "))
for i in range(f):
    M.append([0]*c)
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
