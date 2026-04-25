# range (start stop step)
for i in range(0,11,2): # stetp of 2
    print(i)

print("End of range(0, 11, 2)")

#count down using negative step
for i in range(10,0,-1): #step of -1
    print(i)

print("End of range(10, 0, -1)")

# error: step of 0 is not allowed
for i in range(0, 10, 0): # step of 0
    print(i)