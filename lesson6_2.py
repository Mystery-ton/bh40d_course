# Код Морзе для представления цифр и букв использует тире и точки. Напишите
# функцию для кодирования текстового сообщения в соответствии с кодом Морзе.
# (словари в помощь

azbuka_morze = {"a": ".-", "b": "-...", "c": "-.-.", " ": " "}


def translate(text):
    res_list = []
    for i in text:
        res_list.append(azbuka_morze.get(i))
    res = " ".join(res_list)
    return res


text = input("Enter text: ")
print(translate(text))
