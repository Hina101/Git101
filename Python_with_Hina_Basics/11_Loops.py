#while and for loops

#while loops

# x=0
# while(x<5):
#     print(x)
#     x=x+1

# x=0
# while(x<=5):
#     print(x)
#     x=x+1    

#for loop

# for x in range(4,11):
#     print(x)  

#array

# days = ["Mon", "Tues", "Thu", "Fri",  "sat", "Sun"]

# for d in days:
#     print(d)

#use if else

days = ["Mon", "Tues", "Thu", "Fri",  "sat", "Sun"]

for d in days:
    # if(d=="Fri"):break #loop
    if(d=="fri"):continue #skips d
    print(d)
   