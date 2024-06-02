x=4             #Ingeter
y=10.5          #float
z="Hello"       #string


# x=x*y        #Float
# x=x+y        #float
# x=y/x        #float


#implicit_type_conversion

x=x+y 
print(x,"type_of_x_is;",type(x))

#explicit_type_conversion

age=input("What_is_your_age?    ")
age=int(age)                    
print(type(age))              #other way (without step 2)  
print(type(int(age)))         #integer
print(age,type(int(age)))     #if we pet age=14.5       answer will b invalid (float)
print(age,type(float(age)))   #float
print(age,type(str(age)))       #string



name=input("what_is_your_name?     ")
print(name,type(str(name)))