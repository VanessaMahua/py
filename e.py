'''n=int(input("n?: "))
menor=20
c=s=mayor=0
while n!=-1:
	
	if  n<menor:
		menor=n
	if n>mayor:
		
		mayor=n
	
	s+=n
	c+=1
	n=int(input("n?:"))
promedio=(s-menor+mayor)/c
print("Elpromedio es : ", promedio

s=c=0
menor=20
mayor=0

n=int(input("n?: "))
if n>=0 and n <=20:
	
	while n!=-1:
		
		if  n<menor:
			menor=n
		if n>mayor:
		
			mayor=n
		s+=n
		c+=1
		n=int(input("nota"))
promedio=s/c
print (s)
print("Elpromedio es : ", promedio,mayor,menor)

n=int(input("n?"))

c=0
s=1
while c<n:
	s+=c
	
	print (" "),s,
	c+=1'''


n=int (input("n"))
if n>0:
	c=0
	s=0
	while n!=0:
		modulo=n%10
		n=n//10
		s+=modulo
		c+=1
print ("dfbn",s, s/c)'''0
