# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

data = {
    "Belarus": ["Minsk", "Grodno", "Brest"],
    "USA": ["Vashington", "New York", "Kanzas"],
}


def it_is_into(city, data):
    answer = "There is no such information."
    for i in data:
        if city in data[i]:
            answer = i

    return answer


print(it_is_into("New York", data))
