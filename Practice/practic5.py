
print("ADD USERS / PASSWORDS")
users = []
password = []

while True:
    admin = input("add users: ")

    if admin == "stop":
        break
    else:
        users.append(admin)
print("Users list ", users)

user_login = input("check index login: ")

if user_login in users:
    print(user_login, " < in the list, under the index:", users.index(user_login))
else:
    print("Error")

while True:
    user_pass = input("add user password: ")

    if user_pass == "stop":
        break
    else:
        password.append(user_pass)
print("Users password list ", password)

pass_check = input("check index password: ")

if pass_check in password:
    print(pass_check, " < in the list, under the index:", password.index(pass_check))
else:
    print("Error")

login = input("enter login: ")

while True:
    if login in users:
        print("login accepted")
        break
    else:
        print("Error")
        break


while True:
    password_user = input("enter password: ")
    if password_user in users[0]:
