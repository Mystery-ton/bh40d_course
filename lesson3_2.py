# Пользователь вводит 3 числа, найти среднее арифмитическое с точностью 3

str_numbers = input("Enter 3 numbers by space to calculate average: ")
str_numbers_list = str_numbers.split()
first = float(str_numbers_list[0])
second = float(str_numbers_list[1])
third = float(str_numbers_list[2])
avg = (first + second + third) / str_numbers_list.__len__()
avg_round = round(avg, 3)
print(f"{avg_round} is average")
