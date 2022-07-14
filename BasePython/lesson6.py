# def say_hello():
#     print("Hello")
#
#
# say_hello()
# say_hello()
# say_hello()


# def say_hello(): print("Hello")
#
#
# say_hello()


# def say_hello():
#     print("Hello")
#
#
# def say_goodbye():
#     print("Goodbye")
#
#
# say_hello()
# say_goodbye()


# def print_message():
#     def say_hello():
#         print("Hello")
#     def say_goodbye():
#         print("Goodbye")
#     say_hello()
#     say_goodbye()
#
#
# print_message()


# def say_hello():
#     print("Hello")
#
#
# def say_goodbye():
#     print("Goodbye")
#
#
# def main():
#     say_hello()
#     say_goodbye()
#
#
# main()


# def say_hello(name):
#     print("hello", name)
#
#
# say_hello("Alex")
# say_hello("Olha")
# say_hello("Petro")


# def print_info(name, age):
#     print("name:", name)
#     print("age:", age)
#
#
# print_info("Oleksandr", 37)
# print_info("Agnieszka", 30)
# print_info("Vasil", 60)
# print_info("Dimon", 18)


# def name_info(name, age):
#     print("name:", name)
#     print("age:", age)
#
#
# while True:
#     info_name = input("введіть імя: ")
#     info_age = int(input("введіть роки: "))
#     name_info(info_name, info_age)


# def calc_result(a, b, c):
#     # print("a:", a)
#     # print("b:", b)
#     # print("c:", c)
#     print(a + b - c)
#
#
# while True:
#     result_a = float(input("enter value <a> : "))
#     result_b = float(input("enter value <b> : "))
#     result_c = float(input("enter value <c> : "))
#     calc_result(result_a, result_b, result_c)


# def say_hello(name="User"):
#     print("Hello", name)
#
#
# say_hello("Alex")


# def print_info(name=, age=18):
#     print(name, age)
#
#
# print_info("Olia", 20)


# def print_info(name, text):
#     print(f"my name is {name} today i want tell you some info: {text}.")  # f - форматована строка.
#
#
# print_info("Alex", "my birthday today")


# def sum(*numbers):
#     result = 0
#
#     for i in numbers:
#         result += i
#
#     print(f"result = {result}")
#
#
# sum(1, 2, 3)


# def world_text(*text):
#     result = ""
#
#     for i in text:
#         result += i
#     print(result)
#
#
# a = ""
# while True:
#     finally_text = input("Enter any text: ")
#     if finally_text == "stop":
#         break
#     else:
#         a += " "
#         a += finally_text
#
#
# world_text(a)


# def f(x):
#     if x <= -2:
#         print(1 - (x + 2)**2)
#     elif - 2 < x <= 2:
#         print(- x / 2)
#     elif 2 < x:
#         print((x - 2)**2 + 1)
#
#
# value = float(input("enter value: "))
#
# f(value)
#

# numbers = []
#
#
# def modify_list(l):
#     for i in l:
#         if i % 2 == 0:
#             numbers.append(i // 2)
#
#     l[:] = numbers
#     print(l)
#
#
# modify_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# def update_dictionary(d, key, value):
#     if key in d:
#         d[key].append(value)
#         print(d)
#     elif key is not d:
#         if 2 * key is d:
#             d[2 * key].append(value)
#             print(d)
#         elif (2 * key is not d) and d.get(2 * key) is None:
#             d[2 * key] = []
#             d[2 * key].append(value)
#             print(d)
#
#
# name = {
#     1: [1, 2]
# }
#
# update_dictionary(name, 1, "value")


# 1) Написати функцію яка приймає два параметра число a і число b та прінтує їхню суму.


# def calc_res(a, b):
#     print(a + b)
#
#
# calc_res(5, 5)


# 2) Написати функцію яка приймає вік та ім'я, параметр ім'я має значення по стандарту. Та виводить:
# Привіт, мене звати <name>, мені <age> років.


# def people_info(age, name="Alex"):
#     print("Привіт мене звати,", name, "мені", age, "років.")
#
#
# people_info(12, "Dimon")


# Написати функцію яка приймає безліч параметрів та виводить їх суму.
# (Безліч параметрів це *params)


# def result_info(*params):
#     a = 0
#
#     for i in params:
#         a += i
#
#     print(a)
#
#
# result_info(1, 2, 3, 4)


# params = [1, 2, 3, 4, 5, 6]
# a = 0
# for i in params:
#     a += i
# print(a)


# 4) Андрій працює на двох роботах на яких помісячна
# зарплатня. І має певні розходи на життя в місяць.
# Написати функцію яка підрахує скільки грошей залишається в Андрія після прожитого місяця.


# job1 = int(input("Зарплата першої роботи: "))
# job2 = int(input("Зарплата другої роботи: "))
# spend = int(input("Скільки витрачаю в місяць: "))
#
#
# def job_money(job1, job2, spend):
#     print(job1+job2-spend)
#
#
# job_money(job1, job2, spend)


