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

user = {
    "Oleksandr": "Polishchuk",
    "Agnieszka": "Knap",
    "John": "Traworla",
    "Olha": "Tverdochlib",
    "Ivan": "Danyliv"
}
# print(user["Oleksandr"])
print(user.get("John"))
