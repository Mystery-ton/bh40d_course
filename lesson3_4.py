# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных.

text = input("Enter 3 numbers by space to count positive and negative: ")
negative_num = text.count("-")
positive_num = 3 - negative_num
print(f"Number of negative: {negative_num} \nNumber of positive: {positive_num}")
