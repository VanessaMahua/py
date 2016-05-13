x=int(input("Cantidad (x)"))
cont_per=0
num=6
while True:
	s=0
	for i in range (num//2+1):
		if num%i==0:
			s=s+i
	if s==num:
		print (num)
		cont_per=cont_per+1
	if con_per == x:
		break
	num+=1
