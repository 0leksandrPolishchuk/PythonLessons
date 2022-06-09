users_pass = [["Oleksandr", "Alex1985"], ["Alan", "AlanAlan"],
              ["Agnieszka", "1988"], ["Emma", "2013"], ["Daniel", "2010"]]
test = False

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
        print("Error!")
        break

if not test:
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




# users_pass = [["Oleksandr", "Alex1985"], ["Alan", "AlanAlan"],
#               ["Agnieszka", "1988"], ["Emma", "2013"], ["Daniel", "2010"]]
#
#
# for i in users_pass:
#     print("Password: ", i[1])
#     print("Login: ", i[0])
# if i in users_pass:
#     print("Password: ", i[1])




#
#
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
