first_num = float(input("Enter first number: "))
operation = input("Enter operation: ")
second_num = float(input("Enter second number: "))

if operation == "+":
    print(first_num + second_num)
elif operation == "-":
    print(first_num - second_num)
elif operation == "*":
    print(first_num * second_num)
else:
    print("There is no such operation.")
