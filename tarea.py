def departamentos():
	esc=open("departamento.txt","w")
	esc.write("DEPARTAMENTOS \n")

	n=int(input("cantidad de departamentos? "))

	for i in range(n):
		departamento=input("Departamento = ")
		provincia=input("Num de provincias= ")
		esc.write(departamento)
		esc.write(" : ")	
		esc.write(provincia)	
		esc.write("\n")
	esc.close()
	
	lec=open("departamento.txt","r")
	dep=input("Departamento buscado: ")
	prueba=lec.read()
	linea=prueba.split()
	for i in range(len(linea)):
		if linea[i]==dep:
			print(dep,"tiene",linea[i+2],"provincias")
	else:
		print("No exixte departamento")
	lec.close
departamentos()

	
********************************************************
lectura=open("contenido.txt","r")
nuevo=open("modificado.txt","w")
letra=lectura.read()
for i in range(len(letra)-1,-1,-1):
    nuevo.write(letra[i])
lectura.close()
nuevo.close()
lectura=open("contenido.txt","r")
nuevo=open("modificado.txt","w")
letra=lectura.read()
for i in range(len(letra)-1,-1,-1):
    nuevo.write(letra[i])
lectura.close()
nuevo.close()
lectura=open("contenido.txt","r")
nuevo=open("modificado.txt","w")
letra=lectura.read()
for i in range(len(letra)-1,-1,-1):
    nuevo.write(letra[i])
lectura.close()
nuevo.close()
***************************************************
lectura=open("contenido.txt","r")
nuevo=open("FileX.txt","w")
letras=lectura.read()
c=0
new=" "
if letras!=" ":
        c+=1
for m in letras:
    if m!=" " :
        let=str(m)
  
        new.append(let)
        print(new)
    else:
        nuevo.write(m)
      
        
lista_letras=letras.split()

#for letra in lista_letras:
#        for i in range(len(letra)-1,-1,-1):
#            nuevo.write(letra[i])
 #       nuevo.write(" ")
lectura.close()
nuevo.close()
