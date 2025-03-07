# this gets you to 16 rather then 15 (I tried my best to learn implement shifting but this is a new concept for me)

#What I Learned Today: 
#We can use "<<" in python for shifting left and ">>" for shifting right.
#We can use shifting with binary numbers. We can convert regular number to binary.
#Left shiffting will multtiply it by two each time you shift it 
# I am not completly sure but based on this I would guess that a right shift will divide by 2??

def multiply(n):
    n = 1
    n = n + 1
    return n << 3
print(multiply(5))
