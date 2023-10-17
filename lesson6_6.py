# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные


# def chet_first(nums):
#     if nums[0] % 2 == 1:
#         i = nums.pop(0)
#         nums.append(i)
#     return nums


nums = [1, 3, 2, 4, 6, 9, 17, 13, 14]
nums.sort(key=lambda x: x % 2)
print(nums)

# for i in range(0, len(nums) + 1):
#     chet_first(nums)
# print(nums)
