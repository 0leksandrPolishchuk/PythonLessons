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


# name = "Alan"
#
#
# def say_hello():
#     print("Hello,", name)
#
#
# def say_bye():
#     print("See you later,", name)
#
#
# say_hello()
# say_bye()
#
# print(name)


# def say_hello():
#     name = "Oleksandr"
#     surname = "Polishchuk"
#     print("Hello, my name is,", name + ".", "My surname,", surname + ".")
#
#
# def say_bye():
#     name = "Dimon"
#     surname = "Petrovich"
#     print("See you later,", name, surname + ".")
#
#
# say_hello()
# say_bye()


# name = "Oleksandr"
#
#
# def say_hello():
#     global name
#     name = "Serhii"
#     print("Hello", name + ".")
#
#
# def say_bye():
#     print("See you later,", name + ".")
#
#
# say_hello()
# say_bye()
# print(name)


# Всім відомо, що математичне число PI = 3.14.
# Але після глобальної катастрофи значення числа PI змінилося на PI = 7.2. Описати функції які вираховують площі кола
# (формула S = P * R в квадраті) до катастрофи і після катастрофи.
# В результаті число PI повинно набути нового значення назавжди.


# PI = 3.14
#
#
# def a_inf(r):
#     return PI * r ** 2
#
#
# def b_inf(r):
#     global PI
#     PI = 7.2
#     return PI * r ** 2
#
#
# print(a_inf(4))
# print(b_inf(4))
# print(PI)


# Андрій відкрив IT компанію з назвою "ЯблукоIT". Але пізніше
# з'явилася змога працювати з американсьми замовниками і він був змушений провести
# ребрендінг компанії на "AppleIT". Описати дві функції, які виводять інформацію для замовників до і
# після ребрендінгу. Напиклад:
# 1) Привіт, я представник ЯблукоIT
# 2) Hi, I'm a representative AppleIT (Замість Hi, I'm a representative ЯблукоIT)


# company_name = "ЯблукоIT"
#
#
# def a():
#     print("Привіт я представник", company_name + ".")
#
#
# def b():
#     global company_name
#     company_name = "AppleIT"
#     print("Hi, Im a representative", company_name + ".")
#
#
# def c():
#     print(company_name, "Допоможе вирушити вам ваші найскладніші задачі.")
#     print(company_name, "Працює за допомогою технології Python.")
#
#
# def d():
#     print(company_name, "Співпрацює лише з досвідченими розробниками.")
#     print("Штаб", company_name, "Налічує понад 100 спеціалістів.")
#
#
# a()
# b()
# c()
# d()


# def outer():
#     n = 5
#
#     def inner():
#         print(n)
#
#     inner()
#     print(n)
#
#
# outer()


# def outer():
#     n = 5
#
#     def inner():
#         n = 25
#         print(n)
#
#     inner()
#     print(n)
#
#
# outer()


# def outer():
#     n = 5
#
#     def inner():
#         nonlocal n
#         n = 25
#         print(n)
#
#     inner()
#     print(n)
#
#
# outer()


