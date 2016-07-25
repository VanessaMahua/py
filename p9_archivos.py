#1 esc.write =("hola") -->Mal !!! quitar el ("=")
# no olvidar cerrar lo abierto
'''
esc=open("ar.txt","w")
esc.write("Hola \n")
esc.write(" soy mahua \n")
esc.write("________")
esc.close()
'''
#2 y 3 #si coloco linea antes del while bucle infinito
'''
lec=open("ar.txt","r")
while True :
    linea=lec.readline()
    if  len(linea) == 0:
        break
    else:
        print(linea)
lec.close()
#Pedir a N usuarios su nombre y edad y guardar los datos en el archivo "Data.txt"
#esc.write(nombre+":"+edad+"\n")
esc=open("Data.txt","w")
n=int(input("N?: "))
for i in range(n):
        nombre=input("Nombre: ")
        edad=input("Edad: ")
        esc.write(nombre+":"+edad+"\n")
esc.close()
'''
#Retornar el contenido de un archivo en una lista  cada linea es un elemento
#fijese readlines esta en plural
#fichero.seek(0) en read & readline
'''
lec=open("Data.txt","r")
xs=lec.readlines() #lista con readl9ines
lec.close()# libero memoria
xs.sort()#ordena forma creciente
esc=open("DataOnd.txt","w")
for i in xs:
        esc.write(i)
esc.close()
'''
# read lee todo como string , readline lee lines* linea , readlines convierte lista
#leer todo el contenido como una cadena
'''
lec=open("Data.txt")
contenido=lec.read()#convierte a string
print(contenido)
lec.close()
palabras=contenido.split()# fracciona mediante espacios
print(palabras)
print("hay", len(palabras)," palabras")
'''

#4
'''
lec=open("ar.txt","r")
esc2=open("ar2.txt","w")
contenido=lec.read()
for i in contenido:
    if i == " ":
        esc2.write("*")
    else:
        esc2.write(i)
lec.close()
esc2.close()
'''
#5 esc2.write(palabras[c]+"\n") para pegar por columan se concatena
#solo lee palabras  split, ojo con "r"
'''
esc=open("rayuela.txt","w")
esc.write("Va\n")
esc.write("23\n")
esc.write("De\n")
esc.write("17\n")
esc.write("Ed\n")
esc.write("18")
esc=open("rayuela.txt","r")
esc1=open("R1.txt","w")
esc2=open("R2.txt","w")

tam=esc.read()

palabras=tam.split()
c=0
while c<len(palabras):
    if c%2==0:
        esc2.write(palabras[c]+"\n")
              
    else:
        esc1.write(palabras[c]+"\n")
    c+=1
esc.close()
esc1.close()
esc2.close()
'''
#6 ver el while forget condicion
# 
'''
esc=open("file.txt","w")
cad=input("Ingrese cadena ?:")
while cad!= " ":
    esc.write(cad+"\n")
    cad=input("Ingrese cadena ?:")
esc=open("file.txt","r")
while True:
    palabra=esc.readline()
    if len(palabra)== 0:
        break
    else:
        print (palabra)
esc.close()
'''
#7-8-9 el split lo vuelve string asi que puedes verlo con posiciones
'''
esc=open("file2.txt","r")
contenido=esc.read()
linea=0
n_palabras=0
palabras=contenido.split()
for i in range(len(contenido)):
    if contenido[i]=="\n":
        linea+=1
for i in palabras:
    n_palabras+=len(i)

        
print("lineas",linea)
print("n_caracteres",n_palabras)
print("N° palabras", len(palabras))
print("palabras",palabras)
esc.close()
'''
#10
