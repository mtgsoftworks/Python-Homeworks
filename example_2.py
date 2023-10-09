from fibonacci import fibonacci

total = 0

list = fibonacci(100,1)

for num in list:  
    if num % 2 != 0:
        total += num

print("Result: " + str(total))
       
       

