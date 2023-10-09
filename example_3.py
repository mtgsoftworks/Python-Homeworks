n1 = 0
n2 = 0
total = 0

for i in range(1,101):#Square of the sum of the first 100 natural numbers
    n1 += i
n1 = pow(n1,2)

for a in range(1,101):#Sum of Squares of First 100 Natural Numbers
    n2 += pow(n2,2)

total = n1 - n2
print("Result: " + str(total))

