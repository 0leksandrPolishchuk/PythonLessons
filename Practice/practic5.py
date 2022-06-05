#
# print("ADD USERS / PASSWORDS")
# users = []
# password = []
#
# while True:
#     admin = input("add users: ")
#
#     if admin == "stop":
#         break
#     else:
#         users.append(admin)
# print("Users list ", users)
#
# user_login = input("check index login: ")
#
# if user_login in users:
#     print(user_login, " < in the list, under the index:", users.index(user_login))
# else:
#     print("Error")
#
# while True:
#     user_pass = input("add user password: ")
#
#     if user_pass == "stop":
#         break
#     else:
#         password.append(user_pass)
# print("Users password list ", password)
#
# pass_check = input("check index password: ")
#
# if pass_check in password:
#     print(pass_check, " < in the list, under the index:", password.index(pass_check))
# else:
#     print("Error")
#
# login = input("enter login: ")
#
# while True:
#     if login in users:
#         print("login accepted")
#         break
#     else:
#         print("Error")
#         break
#
#
# while True:
#     password_user = input("enter password: ")
#     if password_user == users[0]:
#         # x = password.index(password_user)
#         # if password_user == password[x]:
#         print("Good")
#         # else:
#         #     print(False)
#
#

# user = [['a', 1], ['b', 2], ['b', 3]]
# print(user)
# print(user[0])
# print(user[0][1])


# user = {
#     'Serhii': 123456,
#     'Ahmed': 345234,
#     'Oleg': 3241421
# }
#
# print(user)
#
# while True:
#     q = input("Please input user name:")
#     pas = int(input("Please input user password: "))
#     if pas == user.get(q):
#         print('User', q, 'autorisate')
#         break
#     else:
#         print('Error autorizations')
#         print('Спробуйте ще раз!')


# peoples = ["Alan", "Dima", "Vasia", "Diana"]
# del peoples[0:2]
# print(peoples)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, ]
# numbers = list(range(11))
# print(numbers)
# print(numbers[3:])
# print(numbers[3:6])
# print(numbers[:6])
# print(numbers[::])
# print(numbers[0:8:2])


# for i in range(11):
#     print(i)
# for i in range(5, 11, 2):
#     print(i)


# peoples = ["Galia", "Serhii", "Valodia", "Taras", "Valodia"]
# print(peoples.count("Valodia"))


# numbers = [5, 50, 37, 80, 24, 45, 2, 100]
# print(sorted(numbers))
# print(numbers)
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)

# people = ["Tom",  "bob",  "alice",  "Sam",  "Bill"]
# people.sort()
# print(people)


# people = []
#
# while True:
#     name = input("Please input name: ").lower()
#     if name == "stop":
#         break
#     else:
#         people.append(name)
#
# print(people)
# people.sort()
# print(people)


# numbers = [3, 67, 13, 45, 80, 20, 94, 22, 30]
# print(numbers)
# print(max(numbers))
# print(min(numbers))


# people1 = [45, 13, 10]
# people2 = [20, 50, 90]
# people3 = people1 + people2
# print(people3)
# people3.sort()
# print(people3)

users = [
    ["Oleksandr", 37, 1985],
    ["Inna", 38],
    ["Emma", 9]
]
print(users)
print(users[-1][0])
print(users[1][0])
print(users[0][2])









