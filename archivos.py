#escribir en un archivo
esc=open("miarchivo.Txt","w")
esc.write("Primer Archivo escrito desde Python\n")
esc.write("_________\n")
esc.write("hello \n")
esc.close()


------------------------------------------------------

#leer la informacion de un archivo
lec=open("miarchivo.Txt","r")
while True:
        linea=lec.readline()
        if len(linea)==0:
                break
        print(linea)
lec.close()

---------------------------------------------------------

#Pedir a N usuarios su nombre y edad y guardar los datos en el archivo "Data.txt"
esc=open("Data","w")
n=int(input("N?: "))
for i in range(n):
        nombre=input("Nombre: ")
        edad=input("Edad: ")
        esc.write(nombre+":"+edad+"\n")
esc.close()


---------------------------------------------------------

#Retornar el contenido de un archivo en una lista de lineas
lec=open("Data","r")
xs=lec.readlines()
lec.close()
xs.sort()
esc=open("DataOnd","w")
for i in xs:
        esc.write(i)
esc.close()

---------------------------------------------------------

#leer todo el contenido como una cadena
lec=open("Data")
contenido=lec.read()
print(contenido)
lec.close()
palabras=contenido.split()
print(palabras)
print("hay", len(palabras)," palabras")
