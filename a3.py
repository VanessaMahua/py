'''
class Persona:
             def __init__(self,nombre,edad):
                          self.nombre=nombre
                          self.edad=edad 
                          
p1=Persona("Luis",17)
print("Su nombre es ",p1.nombre,"y su edad es",p1.edad)
'''


'''
class Complejo:
             def __init__(self,real,imag):
                          self.real=real
                          self.imag=imag
             def sumar(self,C2):
                          r=self.real+C2.real
                          i=self.imag+C2.imag
                          C3=Complejo(r,i)
                          return C3
             def restar(self,C2):
                          r=self.real-C2.real
                          i=self.imag-C2.imag
                          C3=Complejo(r,i)
                          return C3
             def mostrar(self):
                          return str(self.real)+"+"+str(self.imag)+"i"
             
C1=Complejo(2,3)
C2=Complejo(3,1)
C3=Complejo(1,1)
C3=C1.sumar(C2)
print("suma= ",C3.real,"+",C3.imag,"i")
C4=C1.restar(C2)
print(C4.mostrar())
'''
'''
class CuentaBancaria:
	def __init__(self,codigo,saldo):
                          self.codigo=codigo
                          self.saldo=saldo
	def depositar(self,s):
		c1.saldo=c1.saldo+s
	
	def consultar(self):
		return c1.saldo

	def retirar(self, r):
		if r> c1.saldo:
			print("Saldo insuficiente")
		else:
			c1.saldo=c1.saldo-r

c1=CuentaBancaria("1000",1500.00)
c1.depositar(300.00)
print("Saldo= ",c1.consultar())
c1.retirar(500.00)
print("Saldo= ",c1.consultar())
'''

class Tiempo:
	def __init__(self,hora,minuto,segundo):
		self.hora = hora
		self.minuto = minuto
		self.segundo = segundo
	def sumar(self,t2):
		
		h=self.hora+t2.hora
		m=self.minuto+t2.minuto
		s=self.segundo+t2.segundo
		t3=Tiempo(h,m,s)
		if s>60:
			print(t3.minuto)
			t3.segundo=t3.segundo+s//60
			t3.minuto=m-60
			print(t3.minuto)
			
		if m>60 :
			print("dsdf")
			t3.hora=t3.hora+m//60
			t3.minuto=m-60
			print(t3.hora)
		
		
		return t3
	def mostrar(self):
                return str(self.hora)+":"+str(self.minuto)+":"+str(self.segundo)

t1=Tiempo(3,20,50)
t2=Tiempo(2,50,30)
t3=t1.sumar(t2)
print(t3.mostrar())	


