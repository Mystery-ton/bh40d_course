# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка


def sum_list(numbers):
    sum = 0
    for i in range(0, len(numbers)):
        if i != len(numbers) - 1:
            sum += numbers[i - 1] + numbers[i + 1]
        else:
            sum += numbers[i - 1] + numbers[0]
    return sum


nums = [1, 8, 0, 5]
print(sum_list(nums))
