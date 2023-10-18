# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно


def str_only(data_list):
    not_str_counter = 0
    for i, val in enumerate(data_list):
        if not isinstance(val, str):
            data_list[i] = 0
            not_str_counter += 1
    for i in range(0, not_str_counter):
        data_list.remove(0)
    return data_list


data = [1, 54, "eree", "1111", {1, 4}]
print(str_only(data))

result = list(filter(lambda x: isinstance(x, str), data))
print(result)

# в вайл оставаться на том же индексе, чтобвы не пропускать значения после удаления
