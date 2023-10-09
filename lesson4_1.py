# Заполнить список степенями числа 2 (от 2^1 до 2^n).

power = int(input("Enter power: "))
pow_list = [pow(2, i) for i in range(1, power + 1)]
print(pow_list)
