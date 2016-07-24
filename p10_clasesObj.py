#1 si quieres varios rectagulos , crear una lista y que itere con el contador
'''
class rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def area(self):
        return self.base*self.altura
    def perimetro(self):
        return "perimeyto"+str(2*(self.base+self.altura))
n=int(input("Rectangulos?: "))
L=[0]*n
for i in range(n):
    b=int(input("Base?: "))
    h=int(input("Altura?: "))
    L[i]=rectangulo(b,h)
    print(L[i].area())
    print(L[i].perimetro())
'''
#2 en los return puedes poner texto  pero las variables int se deben convertir en str
'''
class punto:
    def __init__ (self,x,y,z ):
        self.x=x
        self.y=y
        self.z=z
    def set_x(self,x):
        self.x=x
    def set_y(self,y):
        self.y=y
    def set_z(self,z):
        self.z=z
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_z(self):
        return self.z
    def mostrar(self):
        return str(self.x)+" , "+str(self.y)+" , "+str(self.z)
p1=punto(0,1,2)
print(p1.mostrar())
p1.set_x(3)
print(p1.mostrar())
print(p1.get_x())
'''
#3 (self,x,y) se les iguala  en init , pero para otra funciones  donde se usen otras
#variables como parametros puedes poner otros  nombres de variables no
# necesariamente
'''
class cuentaB:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def depositar(self,d):
        self.y=self.y+d
    def girar(self ,r):
        if r<self.y:
            self.y=self.y-r
            return "cantidad de dinero girado "+str(r)
        else :
            return False
    def consultar(self):
        return self.y
c=cuentaB(1,100)
c.depositar(20)
print(c.girar(80))
print(c.consultar())
'''
#4 self.vectorP=[0]*tam cuantas casillas separa para ingresar datos ya sean int o str
#podemos comprobar que se pueden usar otros names de variables que no esyan en init
#podemos declarar variables con self e inicializarlas tmb
'''
class pila:
    def __init__(self,tam):
        self.tam=tam
        self.top=0
        self.vectorP=[0]*tam
    def push(self,cad):
        self.vectorP[self.top]=cad
        self.top+=1
    def pop(self):
        self.vectorP[self.top]=" "
        self.top-=1
    def mostrar(self):
        for i in range (self.top):
            print(self.vectorP[i])
p1=pila(5)
p1.push("a")
p1.push("b")
p1.mostrar()
p1.pop()
p1.mostrar()
'''
#5 men no necsariamente tiene que ser una variable global ,
# analizar los valores  en el range , think !!!
'''
class fraccion:
    def __init__(self , num , den):
        self.num=num
        self.den=den
    def sumaF(self,f2):
        n=(self.num*f2.den)+(self.den*f2.num)
        d=self.den*f2.den
        f3=fraccion(n,d)
        return f3
    def simplificarF(self):
        
        if self.num<self.den:
            men=self.num
        else:
            men=self.den
        for i in range(2,men+1):
            while self.num%i==0 and self.den%i==0:
                self.num=self.num//i
                self.den=self.den//i
    def mostrar(self):
        return  str(self.num)+" / "+str(self.den)
f1=fraccion(1,2)
f1.mostrar()
f2=fraccion(3,4)
f2.mostrar()
f3=f1.sumaF(f2)
print(f3.mostrar())
f3.simplificarF()
print(f3.mostrar())
'''
#6 print -> "," return-->("+" and str :P)
# Cuando usas un bucle no puedes usar el return , son muchos valores
class tabla:
    def __init__(self,tam):
        self.tam=tam
        self.ent=[0]*tam
        self.cad=[" "]*tam
        self.top=0
    def agregar(self,cad,ent):
        self.cad[self.top]=cad
        self.ent[self.top]=ent
        self.top+=1
    def listar(self):
        for i in range(self.top):
            print  (self.cad[i]), " + ",str(self.ent[i])
    def contar(self,cad):
        c=0
        for i in range(self.top):
            if  self.cad[i][:len(cad)]==cad:
                c+=1
        return c
    def sumar(self,cad):
        c=0
        for i in range(self.top):
            if  self.cad[i][:len(cad)]==cad:
                
                c+=self.ent[i]
        return c
t=tabla(50)

t.agregar("rosa",11)
t.agregar("carlos",20)
t.agregar("rossmary",10)
t.listar()
print(t.contar("ros"))
print(t.sumar("ros"))
