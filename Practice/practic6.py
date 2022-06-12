print("<USER AND PASSWORD VERIFICATION>")

users_pass = [["Oleksandr", "Alex1985"], ["Alan", "AlanAlan"],
              ["Agnieszka", "1988"], ["Emma", "2013"], ["Daniel", "2010"]]
test = False
test1 = False  # Призначення змінної з булевим значенням до блоку, зміни логіну
test2 = False  # Призначення змінної з булевим значенням до блоку, зміни пароля
login1 = "l"
password2 = "p"

# Тут Провіряємо логін та пароль в сприскую
while True:
    login = input(" enter login: ")
    password = input("enter password: ")

    if login in users_pass[0] and password in users_pass[0]:
        print("Accept")
        test = True
        break
    elif login in users_pass[1] and password in users_pass[1]:
        print("Accept")
        test = True
        break
    elif login in users_pass[2] and password in users_pass[2]:
        print("Accept")
        test = True
        break
    elif login in users_pass[3] and password in users_pass[3]:
        print("Accept")
        test = True
        break
    elif login in users_pass[4] and password in users_pass[4]:
        print("Accept")
        test = True
        break
    else:
        print("Error! What you want change, enter l: <login> or  p: <password>")
        break

# Тут вибираємо що будем змінювати.
if not test:
    while True:
        user_or_pass = input("enter option please: ")

        if user_or_pass == password2:
            print("Password selected")
            test2 = True
            break
        elif user_or_pass == login1:
            print("Login selected")
            test1 = True
            break
        else:
            print("Error! ENTER AGAIN")

# Тут Змінюємо пароль.
if not test1:
    while True:
        user_login = input("enter user login, witch  you need change password: ")

        if user_login in users_pass[0]:
            change_pass = input("enter new password: ")

            users_pass[0][1] = change_pass
            print(users_pass)
        elif user_login in users_pass[1]:
            change_pass = input("enter new password: ")

            users_pass[1][1] = change_pass
            print(users_pass)
        elif user_login in users_pass[2]:
            change_pass = input("enter new password: ")

            users_pass[2][1] = change_pass
            print(users_pass)
        elif user_login in users_pass[3]:
            change_pass = input("enter new password: ")

            users_pass[3][1] = change_pass
            print(users_pass)
        elif user_login in users_pass[4]:
            change_pass = input("enter new password: ")

            users_pass[4][1] = change_pass
            print(users_pass)
            break
        else:
            user_login = "Stop"
            print("Done, Password Changed")
            break

# Тут змінюємо логін.
if not test2:
    while True:
        user_login = input("enter login, witch you need change : ")

        if user_login in users_pass[0]:
            change_login = input("enter new login: ")

            users_pass[0][0] = change_login
            print(users_pass)
        elif user_login in users_pass[1]:
            change_pass = input("enter new login: ")

            users_pass[1][0] = change_pass
            print(users_pass)
        elif user_login in users_pass[2]:
            change_login = input("enter new password: ")

            users_pass[2][0] = change_login
            print(users_pass)
        elif user_login in users_pass[3]:
            change_pass = input("enter new login: ")

            users_pass[3][0] = change_pass
            print(users_pass)
        elif user_login in users_pass[4]:
            change_pass = input("enter new login: ")

            users_pass[4][0] = change_pass
            print(users_pass)
            break
        else:
            user_login = "Stop"
            print("Done, Password Changed")
            break


# users_pass = [["Oleksandr", "Alex1985"], ["Alan", "AlanAlan"],
#               ["Agnieszka", "1988"], ["Emma", "2013"], ["Daniel", "2010"]]
# for i in users_pass:
#     print("Password: ", i[1])
#     print("Login: ", i[0])
# if i in users_pass:
#     print("Password: ", i[1])


# numbers = [45, "Alex", 50]
# print(numbers)
# numbers.append(True)
# print(numbers)
# numbers.insert(0, False)
# print(numbers)
# numbers.extend([1, 2, 5])
# print(numbers)
# numbers.remove(False)
# print(numbers)
# numbers.pop(-1)
# print(numbers)
# print(numbers.index(True))
# print(numbers.count("Alex"))
#
#
# numbers = [45, 12, 30, 46, 10, 20, 50]
# numbers.sort()
# numbers.reverse()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
# print(sorted(numbers))
#
#
# numbers = [20, 1, 5, 6, 8, 9, 3]
#
# while True:
#     enter_n = input("enter numbers: ")
#     if enter_n == "stop":
#         break
#     else:
#         numbers.remove(int(enter_n))
#         print(numbers)
