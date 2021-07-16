per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}  # словарь dict
money = int(input("введите сумму "))
per_cent_val = list(per_cent.values())
depo = list(map(lambda x: x * money / 100, per_cent_val))
print(depo)
print("максимальная сумма заработка будет " + str(max(depo)))






























# depo = list(map(lambda x: x * money / 100, per_cent_val))
# print(depo)
# print("максимальная сумма заработка будет " + str(max(depo)))

# string = input("Введите числа через пробел:")


# def double(x):
#     return x * 2
#
#
# double2 = lambda x: x * 2
#
# list_of_strings = string.split()  # список строковых представлений чисел
# list_of_numbers = list(
#     map(double2,
#         map(int, list_of_strings)))  # список чисел
#
# print(list_of_numbers)
