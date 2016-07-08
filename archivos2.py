'''
lec=open("miarchivo1.txt", "r")
esc=open("Mi archivo2.txt", "w")
contenido=lec.read()
for i in range (len(contenido)):
        if contenido[i]== " ":
                esc.write("*")
        else:
                esc.write(contenido[i])
lec.close()
esc.close()
'''

#******************************

lec=open("Archivo1.txt", "r") #leer
#esc=open("Archivo2.txt", "w")#escribir
contenido=lec.read()
contar_palabras=contenido.split()#palabras
lineas=0
caracteres=0
print("palabras: ",len(contar_palabras))

for i in range (len(contenido)):
        if contenido[i]== "\n":
                lineas+=1
for i in range (len(contenido)):
        if contenido[i]!= "\n":
                caracteres+=1
        
print("lineas",lineas)
print("caracteres",caracteres)
lec.close()
#esc.close()
