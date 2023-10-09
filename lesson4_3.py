# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

amount = int(input("Enter amount of names you want to add with emails: "))
name_mail_dict = {
    i: {"name": input("Enter name: "), "email": input("Enter email: ")}
    for i in range(amount)
}
print(name_mail_dict)
