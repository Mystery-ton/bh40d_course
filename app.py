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

# data = [{"name": "a", "age": 34}, {"name": "b", "age": 40}, {"name": "c", "age": 10}]
#
# data.sort(key=lambda x: x.get("age"), reverse=True)
# print(min(data, key=lambda x: x.get("age")))
# print(data)


# def step_gen(number, start, end):
#     for i in range(start, end + 1):
#         yield pow(number, i)
#
#
# for i in step_gen(2, 3, 6):
#     print(i)

# words = ["adg", "Erbgb", "Gvbg", "efvs"]
# words.sort(key=str.lower())
# #words.sort(key=lambda x: x.lower())
# print(words)


# objs = ["iu", "wdicodwcdw", "oijion", "anton", "operator"]
#
# def paginator(objs, page, paginate_by):
#     return objs[page * paginate_by - paginate_by : page * paginate_by]
# print(paginator(objs, 2, 2))


# def min_divisor(num):
#     for i in range(2, num+1):
#         if not num % i:
#             return i
#
# print(min_divisor(1131))

# text = "asdJHHbPOo"


# def upper_count(text):
#     counter = 0
#     for i in text:
#         if i.isupper():
#             counter += 1
#     return counter
#
#
# print(upper_count(text))


# def factorial(number):
#     if number > 1:
#         return number * factorial(number - 1)
#     return number
#
# print(factorial(5))
# def descending_order(num):
#     ans = str(num)
#     # ans.sort(key=int, reverse=True)
#     ans = int("".join(sorted(ans, reverse=True)))
#     return ans
#
#
# print(descending_order(123))
# str = "Ffpjj"
# print(len(str))
# print(len(set(str)))
# print
# filter()


# def solution(s):
#     s = list(s)
#     print(s)
#     i = 0
#     while i in range(0, len(s)):
#         print(s[i])
#         if s[i].isupper():
#             s.insert(i, " ")
#             i += 1
#         i += 1
#     return "".join(s)
#
#
# print(solution("helloWorld"))


# def cakes(recipe, available):
#     cake = 0
#     # possible = True
#     while not ("no" in available.values()):
#         for i in recipe:
#             print(i)
#             if i in available and available[i] >= recipe[i]:
#                 available[i] = available[i] - recipe[i]
#                 if available[i] <= 0:
#                     available[i] = "no"
#             else:
#                 # if available[i] <= 0 or not (i in available):
#                 available[i] = "no"
#                 cake -= 1
#                 break
#         cake += 1
#     return cake
#
#
# print(
#     cakes(
#         {"flour": 500, "sugar": 200, "eggs": 1},
#         {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200},
#     )
# )
# d = {"flour": 500, "sugar": 200, "eggs": 1}
# d2 = {"flour": 1200, "sugar": 1200, "milk": 200, "eggs": 5}
# print(d.values())
# print(d2.values())
# dict.get()
# int.bit_count()


class Product:
    """Класс представления товара"""

    def __init__(self, name: str, descr: str, price: float | int):
        """Object atributes initialization

        :param name: Название товара
        :param descr: Описание товара
        :param price: Цена товара
        """
        if not isinstance(name, str):
            raise ValueError
        if not isinstance(descr, str):
            raise ValueError
        if not isinstance(price, (float, int)):
            raise TypeError
        if price < 0:
            raise ValueError

        self.name = name
        self.descr = descr
        self.price = price

    def dump(self):
        """Сериализация объекта

        :return: Словарь с данными объекта
        """
        return {"name": self.name, "descr": self.descr, "price": self.price}

    def __str__(self) -> str:
        return f"{self.name},{self.price},{self.descr}"

    # def __bool__(self):
    #     return bool(self.price)

    def __len__(self):
        return round(self.price)

    def __getitem__(self, item):
        return self.name[item]

    # def iter(self):
    #     return self
    #
    # def __next__(self):
    #     self.i+=1
    #     if self.i<len(self.name):
    #         return self.name[self.i]
    #     else:
    #         self.i =-1
    #         raise StopIteration

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price
        elif isinstance(other, (int, float)):
            return self.price == other
        raise TypeError
