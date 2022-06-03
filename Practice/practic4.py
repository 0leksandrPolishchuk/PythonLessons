# a = ["Alex", 2, 3.5, "Ukraine", "Petro", "Mama"]
# print(a[0], a[-1])


# cars = ["Ford", "Lexus", "Toyota", "Tesla", "Audi"]
# select_car = input("Please select car: ")
# if select_car in cars:
#     print(True)
# else:
#     print(False)


# cars = ["Ford", "Lexus", "Toyota", "Tesla", "Audi"]
#
# while True:
#     select_cars = input("Please select car: ")
#     if select_cars in cars:
#         print(True)
#     elif select_cars == "Stop":
#         break
#     else:
#         print(False)


# numbers = [2, 1.0, 5, 50, 300, 30.0]
# for i in numbers:
#     print(i / numbers[0])


# numbers = [2, 1, 5, 50, 300, 30]
# question = int(input("Enter your value: "))
# print(numbers[question] / 10)


# n = int(input("Enter number: "))
# print(n + n * n + n * n * n)

# while True:
#     a = int(input("Enter number: "))
#
#     if a % 2 == 0:
#         print("Парне")
#     else:
#         print("Не парне")
#         break


# numbers = [11,  22,  44, 12,  23, 22, 1442, 2466, 23, 237, 11, 12, 13, 14]
# for i in numbers:
#     if i == 237:
#         break
#     elif i % 2 == 0:
#         print(i)


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i <= 5:
#         print(i)


# print("  |REGISTRATION|")
# print("input limit 3 times ")   # Ліміт реєстрації, пароль та логін адміністратора.
# print("-------------------")
#
# admin = input("enter new admin: ")
#
# while True:
#     admin_repeat = input("enter admin again: ")
#
#     if admin_repeat == admin:
#         print("Successfully")
#         break
#     elif admin_repeat != admin:
#         print("<!!! 2 attempts left !!!>")
#     admin_repeat2 = input("enter new admin again: ")
#
#     if admin_repeat2 == admin:
#         print("Successfully")
#         break
#     elif admin_repeat2 != admin:
#         print("<!!! 2 attempts left !!!>")
#     admin_repeat1 = input("enter new admin again: ")
#
#     if admin_repeat1 == admin:
#         print("Successfully")
#         break
#     elif admin_repeat1 != admin:
#         print("Registration Locked")
#         break
#
# password = input("enter new password: ")
#
# while True:
#     password_repeat = input("enter password again: ")
#
#     if password_repeat == password:
#         print("Successfully")
#         break
#     elif password_repeat != password:
#         print("<!!! 2 attempts left !!!>")
#     password_repeat1 = input("enter password again: ")
#
#     if password_repeat1 == password:
#         print("Successfully")
#         break
#     elif password_repeat1 != password:
#         print("<!!! 1 attempts left !!!>")
#     password_repeat2 = input("enter password again: ")
#
#     if password_repeat2 == password:
#         print("Successfully")
#         break
#     elif password_repeat2 != password:
#         print("Registration Locked")
#         break


# a = 1
# b = 2
# a, b = b, a
# print(b, a)


# users = ["Alan", "Dima", "Danik", "Emma", "Petro"]
# x = input("input user: ")
#
# if x in users:
#     print(True)
# else:
#     print(False)

#Приймаєм дані від користувача, та записуєм їх в список(list).
# users = []
#
# while True:
#     user = input("please input you name: ")
#     if user == "stop":
#         break
#     else:
#         users.append(user)
#
# print(users)


















