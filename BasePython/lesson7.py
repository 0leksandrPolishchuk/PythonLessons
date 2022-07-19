# def num_res(a, b):
#     return a + b
#
#
# c = num_res(2, 3)
# print(c)


# def num_res(a, b):
#     print(a + b)
#
#
# c = num_res(5, 10)
# print(c)


# def number_inf(numer):
#     return numer ** 2
#
#
# print(number_inf(2))


# def numbers_inf(a, b):
#     return a * b
#
#
# f = int(input("Enter first number: "))
# s = int(input("Enter second number: "))
#
# print(numbers_inf(f, s))


# def name_inf(name):
#     return "Hello my name", name
#
#
# print(name_inf("Alex"))


# def user_inf(name, age):
#     if age >= 18:
#         return "Доступ дозволено"
#     else:
#         return "Доступ заборонено"
#
#
# n = input("Enter name: ")
# a = int(input("Enter you age: "))
#
#
# print(user_inf(n, a))


# def number_inf(a, b):
#     return a + b
#
#
# while True:
#     f = int(input("Enter first number: "))
#     s = int(input("Enter second number: "))
#     if f == 0:
#         print("Обробка данних завершена. ")
#         break
#     else:
#         print(number_inf(f, s))


# def f(x):
#     if x <= -2:
#         return 1 - pow((x + 2), 2)
#     elif -2 < x <= 2:
#         return - x / 2
#     elif 2 < x:
#         return pow((x - 2), 2) + 1
#
#
# print(f(1))


# def modify_list(l):
#     a = []
#     for i in l:
#         if i % 2 == 0:
#             a.append(i // 2)
#     return a
#
#
# print(modify_list([5, 4, 10, 3, 2, 11]))


# d_test = {
#     1: [],
#     2: ["Alex", 35]
# }
#
#
# def update_dictionary(d, key, value):
#     if key in d:
#         d[key].append(value)
#     if key is not d:
#         if 2 * key is d:
#             d[2 * key].append(value)
#
#
# update_dictionary(d_test, 1, "Alex")
# print(d_test)

