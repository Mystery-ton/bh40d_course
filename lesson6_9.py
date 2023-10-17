# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

data = {
    "1": {
        "name": "Anton",
        "surname": "Sedenevskiy",
        "tel": "61420",
        "mail": "s@mail.com",
    },
    "2": {"name": "A", "surname": "S", "tel": "61", "mail": ""},
    "3": {"name": "iug", "surname": "ohg", "tel": "765"},
}


def no_email(data):
    for i in data:
        if not (
            (("mail", "") in list(data[i].items())) or "mail" in list(data[i].keys())
        ):
            print(data[i]["name"])
        print(list(data[i].items()))


no_email(data)
