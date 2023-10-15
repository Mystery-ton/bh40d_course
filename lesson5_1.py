amount_of_numbers = int(input("Enter amount of nubers: "))
multipl_number = int(input("Enter number: "))
min_number = int(input("Enter minimal number: "))
i = 0

while i < amount_of_numbers:
    if min_number % multipl_number == 0:
        print(min_number)
        i += 1
    min_number += 1
