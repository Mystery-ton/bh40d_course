# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4

numbers = [1, 2, 3, 4, 5, 6, 7]


def offset(numbers_list, n):
    numbers_list = numbers_list[n + 1 : len(numbers_list) + 1] + numbers_list[0 : n + 1]
    return numbers_list


print(offset(numbers, 2))
