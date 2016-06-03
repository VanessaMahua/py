'''
#Ejercicio 1
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False


print(sleep_in(False, False) )
print(sleep_in(True, False) ) 
print(sleep_in(False, True)  )

print("-------------------------------")
#Ejercicio 2
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False

print(monkey_trouble(True, True)  )
print(monkey_trouble(False, False)  )
print(monkey_trouble(True, False)  )

print("-------------------------------")
#Ejercicio 3
def sum_double(a, b):
  # Store the sum in a local variable
  sum = a + b
  
  # Double it if a and b are the same
  if a == b:
    sum = sum * 2
  return sum
print(sum_double(1, 2)  )
print(sum_double(3, 2) ) 
print(sum_double(2, 2) )

print("-------------------------------")
#Ejercicio 4

def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str

print(not_string('candy')  )
print(not_string('x')  )
print(not_string('not bad') )

print("-------------------------------")
#Ejercicio 5
def missing_char(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back

print(missing_char('kitten', 1)  )
print(missing_char('kitten', 0)  )
print(missing_char('kitten', 4)  )

print("-------------------------------")
#Ejercicio 6
def front3(str):
  # Figure the end of the front
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  return front + front + front 

print(front3('Java')  )
print(front3('Chocolate')  ) 
print(front3('abc')  )

print("-------------------------------")
#Ejercicio 7
def string_times(str, n):
  result = ""
  for i in range(n):  # range(n) is [0, 1, 2, .... n-1]
    result = result + str  # could use += here
  return result

print(string_times('Hi', 2)  )
print(string_times('Hi', 3)  )
print(string_times('Hi', 1)  )

print("-------------------------------")
#Ejercicio 8
def front_times(str, n):
  front_len = 3
  if front_len > len(str):
    front_len = len(str)
  front = str[:front_len]
  
  result = ""
  for i in range(n):
    result = result + front
  return result

print(front_times('Chocolate', 2)  )
print(front_times('Chocolate', 3)  )
print(front_times('Abc', 3)  )

print("-------------------------------")
#Ejercicio 9
def string_bits(str):
  result = ""
  # Many ways to do this. This uses the standard loop of i on every char,
  # and inside the loop skips the odd index values.
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print(string_bits('Hello')  )
print(string_bits('Hi')  )
print(string_bits('Heeololeo')  )
'''

print("-------------------------------")
#Ejercicio 10
def string_match(a,b):
	shorter = min(len(a), len(b))
	count = 0
	for i in range(shorter-1):
		a_sub = a[i:i+2]
		b_sub = b[i:i+2]
		if a_sub == b_sub:
			count = count + 1
	return count
i=input()
j=input()
print(string_match(i,j))
print(string_match('xxcaazz','xxbaaz'))
print(string_match('abc','abc'))
print(string_match('abc','axc'))



print("-------------------------------")
#Ejercicio 11

def lone_sum(a,b,c):
	if a==b==c:
		return 0
	if a==b:
		return c
	if b==c:
		return a
	if a==c:
		return b
	return a+b+c

a=int(input("A? : "))
b=int(input("B? : "))
c=int(input("C? : "))
print(lone_sum(a,b,c))
print(lone_sum(1,2,3))
print(lone_sum(3,2,3))
print(lone_sum(3,3,3))
