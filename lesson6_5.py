# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза\


def reverse_list(listik):
    length = len(listik)
    for i in range(0, length // 2):
        first = listik[i]
        last = listik[(-i) - 1]
        listik[i] = last
        listik[(-i) - 1] = first
    return listik


info = [1, 2, 3, 6, 8, 0, 4, 5]
print(reverse_list(info))
