# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
# ]
# for i in numbers:
#     if i % 2 == 0:
#         print(i)
#     elif i == 237:
#         break


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# for i in a:
#     if i <= 5:
#         print(i)


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []
# for i in a:
#     if i in b:
#         c.append(i)
# print(set(c))


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# print(list(set(a) & set(b)))


# my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
# result = sorted(my_dict, key=my_dict.get)
# result.reverse()
# print(result[:3])


# numbers = [1, 2, 4, 6, 22, 11, 22, 32, 5, 8, 100, 334, 21]
# a = int(input("enter number in list: "))
# if a in numbers:
#     print(numbers.index(a))
# else:
#     print("такого числа в списку немає")


# numbers = [1, 2, 4, 6, 22, 11, 22, 32, 5, 8, 100, 334, 21]
# a = numbers.copy()
# print(a)


# numbers = [1, 2, 4, 6, 22, 11, 22, 32, 5, 8, 100, 334, 21]
# numbers.reverse()
# print(numbers)


# numbers = [1, 2, 4, 6, 22, 11, 22, 32, 5, 8, 100, 334, 21]
# numbers.sort()
# print(numbers)


# numbers = [1, 2, 4, 6, 22, 11, 22, 32, 5, 8, 100, 334, 21]
# while True:
#     user = int(input("enter number: "))
#     if user in numbers:
#         numbers.remove(user)
#         print(numbers)
#     if user == 0:
#         break
# print(numbers)


# numbers = [1, 2, 4, 6, 22, 11, 22, 32, 5, 8, 100, 334, 21]
# numbers.clear()
# print(numbers)


# numbers = [1, 2, 4, 6, 22, 11, 22, 32, 5, 8, 100, 334, 21]
# numbers.extend([50, 40, 45])
# print(numbers)

# numbers = [1, 2, 4, 6, 22, 11, 22, 32, 5, 8, 100, 334, 21]
# numbers.append(500)
# print(numbers)


# numbers = [1, 2, 4, 6, 22, 11, 22, 32, 5, 8, 100, 334, 21]
# print(len(numbers))


# numbers = [1, 2, 4, 6, 22, 11, 22, 32, 5, 8, 100, 334, 21]
# print(max(numbers))


# numbers = []
# while True:
#     user_value = int(input("enter numbers: "))
#     if user_value > 0:
#         numbers.append(user_value)
#         print(numbers)
#     else:
#         print("Добавлення неможливе")
#         break


# user = ("Dima", )
# print(type(user))


# cars = ("Ford", "Opel", "BMW", True, 45, 2.6)
# print(cars[-1])


# cars = ("Ford", "Opel", "BMW", True, 45, 2.6)
# for i in cars:
#     print(i)

# cars = ("Ford", "Opel", "BMW", True, 45, 2.6)
# user = input("enter value: ")
# if user in cars:
#     print(True)

# number = range(10, 22, 2)
# print(list(number))


# users = {
#     1: "Oksanka",
#     2: "Dimon",
#     3: "Valodia"
# }
# print(users)


# numbers = [
#     [1, "Vladimir"],
#     [2, "Oksana"],
#     [3, "Vika"]
#     ]
# numbers_dict = dict(numbers)
# print(numbers_dict)


# name = (
#     (1, "Oksanka"),
#     (5, "Petro"),
#     (6, "Ivan")
# )
# name_dict = dict(name)
# print(name_dict)


# name_surname = {
#     "Oksana": "Petrovna",
#     "Vlad": "Ivanov",
#     "Dimon": "Smirnow",
#     "Olia": "Zacharova"
# }
# print(name_surname.get("Oksana"))
# print(name_surname["Vlad"])


# name_surname = {
#     "Oksana": "Petrovna",
#     "Vlad": "Ivanov",
#     "Dimon": "Smirnow",
#     "Olia": "Zacharova"
# }
# # print(name_surname.pop("Vlad"))
# # print(name_surname)
# del name_surname["Olia"]
# print(name_surname)


# name_surname = {
#     "Oksana": "Petrovna",
#     "Vlad": "Ivanov",
#     "Dimon": "Smirnow",
#     "Olia": "Zacharova"
# }
# for i in name_surname.keys():
#     print(i)


# names = {
#     "ford": {
#         "age": "1987",
#         "colour": "Grey"
#         },
#     "BMW": {
#         "age": "2000",
#         "colour": "Blue"
#     },
#     "Opel": {
#         "age": "2021",
#         "colour": "Red"
#     }
#
# }
# print(names)
# print(names["ford"]["age"])
