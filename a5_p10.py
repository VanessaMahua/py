'''
class fraccion:
	def __init__(self,num,den):
		self.num=num
		self.den=den
	def sumar(self,f2):
		n=self.num*f2.den+self.den*f2.num
		d=self.den*f2.den
		f3=fraccion(n,d)
		return f3
	def simplificar(self):
		men=0
		if self.num<self.den:
			men=self.num
		else:
			men=self.den
		for i in range(2,men+1):
		
			while self.num%i==0 and self.den%i==0 :
				self.num=self.num//i
				self.den=self.den//i


	def mostrar(self):
		return str(self.num)+"/"+str(self.den)
f1=fraccion(2,3)
f2=fraccion(3,5)
f3=f1.sumar(f2)
print("Suma: ",f3.mostrar())
f3.simplificar()
print("Simplificada",f3.mostrar())
'''
'''
	def __init__(self,X,Y,n):
		self.X=X
		self.Y=Y
		self.n=n
	def t(self,n):
		M=[]
		for i in range(n):
			M.append([0]*2)
			'''
class tabla:
	def __init__(self,t):
		self.tam=t
		self.cad=[" "]*t
		self.ent=[0]*t
		self.top=0
	def agregar(self,cad,ent):
			self.cad[self.top]=cad
			self.ent[self.top]=ent
			self.top+=1

	def listar(self):
		for i in range(self.top):
			print (self.cad[i],",",self.ent[i])
	def contar(self,cad):
		c=0
		for i in range(self.top):
			tam=len(cad)
			
			if self.cad[i][:tam]==cad:
				c+=1
		return c
	def sumar(self,cad):
		c=0
		for i in range(self.top):
			tam=len(cad)
			
			if self.cad[i][:tam]==cad:
				c=c+self.ent[i]
		return c
'''
n=int(input("t?: "))

string=input(" Ingrese nombre: ")
valor=int(input("INgrese edad:"))
T=tabla(string,valor,n)
T.agregar("rosa",11)
T.listar()
T.contar("ros")
T.sumar("ros")'''
t=tabla(10)
t.agregar("rosa",11)
t.agregar("carlos",20)
t.agregar("rossmary",10)
print("Cantidad que inician: ",t.contar("ros"))
print("suma de valores: ",t.sumar("ros"))
