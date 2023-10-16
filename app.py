# lesson4

# distance = 100
# days = 1
# while distance < 200:
#     days += 1
#     distance += distance * 0.1
# else:
#     print(days)

# number = int(input())
# simple = True
# for i in range(2, number // 2 + 1):
#     if not(number % i):
#         simple = False
#         break
# print(simple)


# info_list = ["idaxo,235,546", "minsk,67,84"]
# info_dict = {}
# for info in info_list:
#    info_split = info.split(",")
#    info_dict[info_split[0]] = int(info_split[2]) - int(info_split[1])
# print(info_dict)

# info_dict={info_list[i].split(",") for i in info_list}

# lesson6

# cities = ["m", "g", "s"]
# population = [12.3, 5.67, 15.8]
# number = float(input("Enter number: "))
# for i, val in enumerate(population):
#    if number <= val:
#        print(cities[i])

# enumerate() возвращает кортеж с индексом и значением из списка например, индекс доставали в i , а значение в val.

data = [{"name": "a", "age": 34}, {"name": "b", "age": 40}, {"name": "c", "age": 10}]

data.sort(key=lambda x: x.get("age"), reverse=True)
print(min(data, key=lambda x: x.get("age")))
print(data)
