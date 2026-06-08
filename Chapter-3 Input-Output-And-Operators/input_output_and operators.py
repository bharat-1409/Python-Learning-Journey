#Output-print()
name="Bharat"
age=21
print("Helllooo")#Normal/basic just printing the things
print(f"My name is {name} and my age is {age}")#using the formatted string
print("My name is",name,"and my age is",age,)#using multiple values

#input-Input() It is always a string and for int/float we need to convert it manually
#MyAge=input("What is your age-:")
#print(f"My age is {MyAge}")

#YourName=input("What is your name -")
#YourAge=int(input("Age is-"))
#print(f"My name is {YourName} and age is {YourAge}")

#Operators
#1. Arithmetic operators(+.-,/,//,*,**,%) these all follows BODMAS
a=12
b=10
c=24
print(100+a+b-c)
print(a+b+c) #add
print(a-c) #subtract
print(a/b) #divide
print(a//b) # floor division converts float in int after dividing removes the decimal point
print(a**b) #exponential
print(10*5) #multiply
print(34%4) #modulus- returns the remainder
print(77%8)
# BODMAS RULES
"""
1-()
2-**
3-%,*,/,//
4;+-
"""
print(3+2**2*5-1)


#COMPARISON OPERATOR- Always returns True and False)
# (<.>,>=.<=,!=,==)
print(12==23)
print(12==12)
print(80>=12)
print(90!=13)
print(88!=80)
print(23>12)
print(11>12)
print(10<9)

# LOGICAL OPERATORS----AND OR NOT(&&,||,!!)
# USED TO COMPARE MULTIPLE VALUES
print(5==5 and 58>50 and 34<99) #true--when all conditions are true 
print(3==4 or 56==34 or 45==54 or 33==33)# true when one condition is true
print(not(3==3))
print(not(5==5 and 3!=4)or(10>20))

#ASSIGNMENT OPERATORS - Used to assign the values to the variable
h=33
h+=10
h+=11
h+=10

p=10
p-=11
p-=88

i=10
i*=19

o=30
o/=10
o/=3



































