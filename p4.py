def signo(n):
  if n<0:
    return -1
  elif n>0:
    return 1
  else:
    return 0
n=int(input("n"))
print signo(n)

def cuadrado(n):
  return n*n
n=int(input("n"))
print cuadrado(n)

def absolute(n):
  if n<0:
    return n*-1
  return n
n=int(input("n"))
print caudrado(n)

def maximo(a,b,c):
  if a>b and a>c:
    return a
  elif b>a and b>c:
    return b
  else:
    return c
a=int(input("a"))
b=int(input("b"))
c=int(input("c"))
print maximo(a,b,c)    

def dividesto(a,b):
  if b%a==0:
    print("si divide",a,"a".b)
  else:
    print("no divide")
a=int(input("a"))
b=int(input("b"))
dicvidesto(a,b)

def ismultiple(a,b):
  if a%b==0 and a%c==0:
    print("es multiplo",a,a"de",b,c)
  else:
    print("no multiplo")
a=int(input("a"))
b=int(input("b"))
is multiple(a,b)

def is commonmult(a,b,c):
  if a%b==0 and a%c==0:
    print("es multiplo",a,"de",b,c)
  else:
    print("no multiplo")
a=int(input("a"))
b=int(input("b"))
c=int(input("c"))
iscommonmult(a,b,c)

def swap(a,b):
  c=a
  a=b
  print("a=",a;"b=",b)
a=int(input("a"))
b=int(input("b"))
swap(a,b)

def cortarpos(L):
  c=0
  for i in L:
    if 1>0:
      print(i)
      c+=1
  print(C)
  
n=int(input("cuantos valores"))
c=0
L=[]
whilec<n:
  x=int(input("valor"))
  L.appened(x)
  c+=1
contarpos(L)
