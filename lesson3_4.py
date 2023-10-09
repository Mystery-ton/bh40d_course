# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных.

#text = input("Enter 3 numbers by space to count positive and negative: ")
#negative_num = text.count("-")
#positive_num = 3 - negative_num
#print(f"Number of negative: {negative_num} \nNumber of positive: {positive_num}")

#исправить не через минус, через сравнение с нулем.

a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
a_is_positive= a>0
b_is_positive= b>0
c_is_positive= c>0

a_is_negative= a<0
b_is_negative= b<0
c_is_negative= c>0

pos_count=a_is_positive+b_is_positive+c_is_positive
neg_count=a_is_negative+b_is_negative+c_is_negative
print(f"Negative: {neg_count}; Positive: {pos_count}")

