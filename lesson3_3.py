# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способами.

name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

print(
    "Hello, {name} from {city}. You are {age}!!!".format(name=name, age=age, city=city)
)

print(f"Hello, {name} from {city}. You are {age}!!!")

print("Hello, %s from %s. You are %d!!!" % (name, city, age))
