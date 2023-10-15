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


info_list = ["idaxo,235,546", "minsk,67,84"]
info_dict = {}
for info in info_list:
    info_split = info.split(",")
    info_dict[info_split[0]] = int(info_split[2]) - int(info_split[1])
print(info_dict)

# info_dict={info_list[i].split(",") for i in info_list}
