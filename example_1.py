from fibonacci import fibonacci

order = int(input("Enter the order of elements you want?: "))

result = fibonacci(pow(order,2),1)
print("Result: " + str(result[order]))
