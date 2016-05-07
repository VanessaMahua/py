s=mayor=c=0
menor=20
nota=int(input("nota?"))
if nota >=0 and nota<=20:
   while nota !=-1:
        if nota >10 and nota<=20 :
            if nota <menor:
                menor = nota
            if nota >mayor:
                mayor= nota
                   
        else:
            nota=0
            c-=1
        s+=nota
        c+=1
        nota=int(input("nota?"))
   promedio=s/c
   p=4//3
   print("promdio",promedio,p)
   print("mayor",mayor)
   print("menor",menor)
   
   
        
