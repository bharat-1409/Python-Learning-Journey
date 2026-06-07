
#Unicode Value (ASCII)
a = "h"
print(ord(a))
b = " "
print(ord(b))

#INDEXING

c = "COLLEGE" 
print(c[0])
print(c[2]) # we print  character of strinf And this is positive indexing which strats from 0 and goes from lefty to right
d = "Bharat"
print(d[4],d[-2]) # negative indexing of the string here it goes from right to left


# STRING SLICING(slicing of string means taking out some portion of the string)

slice = "BharatDutta"
h = "ARCHAEOLOGICAL"
q = "COLLEGE"

print(slice[3:6:1]) 
print(h[2:8:1]) 
print(q[0:7:2])
\
# USING DEFAULT CASE EXAMPLE
print(q[::2]) 
print(q[::])

# TASK QUESTION//PRACTISE
a = "Hello how are you" 
print(a[0:5:1])
print(a[6:9:1])
print(a[14:18:1])

#BASIC KNOWLDEGE
a = 10
a = 122
a = 800
print(a) # it will print latest one (a) because python is interprete language and updates the value line by line

# TYPE CONVERSION
a = "12"
print(type(a))

a = int(a)
print(type(a))

a = float(a)
print(type(a))
 
b = "12.3"
b = int(a)
print(b)

c = 12.7
c = float(c)
print(c)
# NOTE--
# You can convert string if it holds valid integer
# you can convert float value to int easily


# Conversion of other types into string
a=1234
b=12.4
c=True
d=12+3j

a=str(a)
b=str(b)
c=str(c)
d=str(d)




