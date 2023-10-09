# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

text = input("Enter sentence: ")
latters_dict = {i: text.count(i) for i in text}
print(latters_dict)
