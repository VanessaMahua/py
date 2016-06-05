def contarPos(L):
	pos=0
	for i in range(len(L)):
		if L[i]>0:
			pos+=1
	return pos
	
		
def contarNeg(L):
	neg=0
	for i in range(len(L)):
		if L[i]<0:
			neg+=1
	return neg	
	


def verificar(L,n):
	
	
	for i in range(len(L)):
		if L[i]==n:
			return True
	return False

def ingresar(L):
	for i in range(len(L)):
		num=int(input("numero "))
		L[i]=num
def mostrar(L):
	for i in range(len(L)):
		print (L[i], "")
n=int(input("N?: "))
L=[0]*n
ingresar(L)

n2=int(input("Valor?: "))
print(verificar(L,n2))
if verificar:
	print("Si")
else:
	print("No")
print("positivos: ",contarPos(L))
print("negativos: ",contarNeg(L))
#9

print("------------------------")

import math 
def ingresar(L):
	for i in range(len(L)):
		num=int(input("numero "))
		L[i]=num
def mostrar(L):
	for i in range(len(L)):
		print (L[i], ' ')



def media(L):
	n=len(L)
	s=0
	for i  in range(n):
		s+=L[i]
	return s/n

def varianza(L):
	n=len(L)
	s=0
	m=media(L)
	for i in range(n):
		s=pow((L[i]-m),2)
	return s/n

def estandar(L):
	v=varianza(L)
	s=v**0.5
	return s
n=int(input("N?: "))
L=[0]*n
ingresar(L)
print("Media= ",media(L))
print("Varianza= ",varianza(L))
print ("D.Estandar= ", estandar(L))
print("------------------------")

#11
print("-------------------------------")
		
def ingresar(L):
	for i in range(len(L)):
		num=int(input("numero "))
		L[i]=num
def veces(L,n):
	c=0
	for i in range(len(L)):
		if L[i]==n:
			c+=1
	return c
n=int(input("N?: "))
L=[0]*n
ingresar(L)
valor=int(input("valor?: "))
veces(L,valor)
print("Cantidad de veces ", veces(L,valor))
print("------------------------")

#12

def ingresar(L):
	for i in range(len(L)):
		num=int(input("numero "))
		L[i]=num
def veces(L):
	
	for i in range(len(L)):
		c=0
		same=L[i]
		for j in range(len(L)):

			if L[j]==same:
			  c+=1
		print (same,"aparece",c,"veces")
n=int(input("N?: "))
L=[0]*n
ingresar(L)

veces(L)

print("------------------------------------------")

#mejorado 12

def ingresar(L):
	for i in range(len(L)):
		num=int(input("numero "))
		L[i]=num
def repetidos(L):
	
	for i in range(len(L)):
		
		same=L[i]
		esta=False
		for j in range(i):
			if same==L[j]:
				esta=True
				break
		if esta==False:
			c=0
			
			for k in range(len(L)):
				
				if L[k]==same:
					  c+=1
			print (same,"aparece",c,"veces")
n=int(input("N?: "))
L=[0]*n
ingresar(L)
#valor=int(input("valor?: "))
#veces(L,valor)
#print("Cantidad de veces ", repetidos(L))


print("------------------------------------------")
def ingresar(L,n):
	for i in range(n):
		num=int(input("numero "))
		L[i]=num

def mostrar(L,n):
	for i in range(n):
		print (L[i], "")


def desplazar(L,n):
	for i in range(n-1,-1,-1):
		L[i+2]=L[i]

n=int(input("N?: "))
L=[0]*(n+2)
ingresar(L,n)
desplazar(L)
mostrar(L,n)

print(---------------------------)
#Ejerccicio 14
def ingresar(L):
	for i in range(len(L)):
		num=int(input("numero "))
		L[i]=num
	return L
def mostrar(L):
	for i in range(len(L)):
		print (L[i],end= " ")

def suma(L1,L2,n):
    lis=[0]*n
    for i in range(n):
        lis[i]=L1[i]+L2[i]
    print("La suma de las listas es : ") 
    mostrar(lis)
def multiplicar(L1,L2,n):
    lis=[0]*n
    for i in range(n):
        lis[i]=L1[i]*L2[i]
    print("\nLa multiplicacion de las listas es : ") 
    mostrar(lis)

    
n=int(input("N?: "))
L=[0]*n
lista1=ingresar(L)
print("Ingrese valores para la segunda lista")
lista2=ingresar(L)
suma(lista1, lista2,n)
multiplicar(lista1,lista2,n)
