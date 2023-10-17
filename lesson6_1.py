# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int


def bin_translation(value, to_bin=True):
    trans_res = []
    res = 0
    if to_bin:
        while value >= 1:
            trans_res.append(str(value % 2))
            value //= 2
        trans_res.reverse()
        res = "".join(trans_res)

    else:
        value = str(value)
        i = 1
        while i <= len(value):
            res += pow(2, i - 1) * int(value[-i])
            i += 1

    return res


val = 100
print(bin_translation(val, False))
# print(bin(val))
