#This gets to 16 not 15 because I just learned what this is but I can explain how I got to 16

#What I Learned Today: 
#We can use "<<" in python for shifting left and ">>" for shifting right.
#We can use shifting with binary numbers. We can convert regular number to binary.
#Left shiffting will multtiply it by two each time you shift it 
# right shift will divide by 2
# its very unlikely we will see bitwise operations often as its more theory 

def multiply(n): #i created a procedure
    n = 1 #i set n equal to 1
    n = n + 1 #i incremented n by 1
    return n << 3 # this means that we multiply it by 2 three times because we left shift it three times and each left shift you multiply by 2
print(multiply(5)) #i am printing the final result
