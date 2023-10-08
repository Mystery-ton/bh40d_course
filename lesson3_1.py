# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами.

sentence = input("Enter your sentence: ")


print(sentence.replace(" ", "-"))

sentence_list = sentence.split(" ")
print(sentence_list)
print("-".join(sentence_list))
