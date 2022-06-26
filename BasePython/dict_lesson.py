# user = {
#     1: "Ael",
#     3: "Agnielex",
#     2: "Daniszka",
# }
# print(user)

# user = {1: "Inna", 2: "Olia", 3: "Petro"}
# print(user)

# users = {
#     "Inna": "inna@icloud.com",
#     "Petro": "petro@gmail.com",
#     "Olha": "olha@ukr.net",
# }
# print(users)

# objects = {
#     1: "Dan",
#     "Married": True,
#     3: 100.6
# }
# print(objects)

# a = {}
# print(type(a))

# b = dict()
# print(b)

# user_list = [
#     ["07533748777", "Oleksandr"],
#     ["9809870987980", "Alan"],
#     ["909870987896", "Emma"],
#     ["27635625346", "Olha"]
# ]
# print(user_list)
# print(type(user_list))
#
# print(type(user_dict))
#
# user_dict = dict(user_list)
# print(user_dict)

# user_tuple = (
#     ("12312312", "Vasia"),
#     ("56575685", "Dimon"),
#     ("9877098070", "Petruha")
# )
# print(user_tuple)
# print(type(user_tuple))
# user_dict = dict(user_tuple)
# print(user_dict)

# name = input("Enter your name: ")
# name_dict = {
#     "user": name
# }
# print(name_dict)

# key = input("Enter key: ")
# value = input("Enter value: ")
# name_dict = {
#     key: value
# }
# print(name_dict)

# user = {
#     "Oleksandr": "Polishchuk",
#     "Agnieszka": "Knap",
#     "John": "Traworla",
#     "Olha": "Tverdochlib",
#     "Ivan": "Danyliv"
# }
# # print(user["Oleksandr"])
# print(user.get("John"))

# user = {
#     "Dima": "Gromov",
#     "Vasia": "Pupkin",
#     "Sonia": "Sonkina"
# }
# del user["Vasia"] # del - це оператор.
# print(user)

# user = {
#     "Dima": "Gromov",
#     "Vasia": "Pupkin",
#     "Sonia": "Sonkina"
# }
#
# while True:
#     user_check = input("enter user: ")
#     if user_check in user:
#         del user[user_check]
#         print(user_check, "deleted")
#     else:
#         print(user_check, "not detected")
#     print(user)

# user = {
#     "Dima": "Gromov",
#     "Vasia": "Pupkin",
#     "Sonia": "Sonkina"
# }
# user_check = input("enter user: ")
# print(user.pop(user_check, "not detected"))
# print(user)

# cars = {
#     "Fiat": "Doblo",
#     "Ford": "Mustang",
#     "BMW": "5 Series"
# }
# while True:
#     cars_del = input("car delete enter 5: ")
#     if cars_del == "5":
#         cars.clear()
#         print(cars, "deleted")
#         break
#     else:
#         print("Error, try again")

# city = {
#     "Kiev": "Podol",
#     "Lviv": "400000",
#     "Ternopil": "Verbickogo"
# }
# print(city)
# city2 = city.copy()
# print(city2)

# peoples = {
#     "Alex": "age, 37",
#     "Olia": "age, 50",
#     "Oleh": "age, 30"
# }
# peoples_name = {
#     "Oleksandr": "Polishchuk",
#     "Agnieszka": "Polishchuk",
#     "Alan": "Polishchuk"
# }
# peoples.update(peoples_name)
# print(peoples)
# print(peoples_name)

# peoples = {
#     "Alex": "age, 37",
#     "Olia": "age, 50",
#     "Oleh": "age, 30"
# }
# peoples_name = {
#     "Oleksandr": "Polishchuk",
#     "Agnieszka": "Polishchuk",
#     "Alan": "Polishchuk"
# }
# all_peoples = {}
# all_peoples.update(peoples)
# all_peoples.update(peoples_name)
# print(all_peoples)

# years = {
#     2021: "Alan birthday",
#     1985: "Oleksandr birthday",
#     1988: "Agnieszka birthday"
# }
# for i in years:
#     print(i)

# years = {
#     2021: "Alan birthday",
#     1985: "Oleksandr birthday",
#     1988: "Agnieszka birthday"
# }
# for k, v in years.items():
#     print(k, v)

# years = {
#     2021: "Alan birthday",
#     1985: "Oleksandr birthday",
#     1988: "Agnieszka birthday"
# }
# for i in years.values():
#     print(i)

# users = {
#     "Oleksandr": {
#         "phone": "28-77-48",
#         "email": "oleksandr@icloud.com"
#     },
#     "Agnieszka": {
#         "phone": "0753374599",
#         "email": "agnieszka@gmail.com",
#     },
#     "Petro": {
#         "phone": 7652347254,
#         "email": "petro@gmail.com",
#     }
# }
# print(users)
# print(users["Oleksandr"])
# print(users["Oleksandr"]["email"])
#
#
# for i in users.values():
#     for j in i.values():
#         print(j)
