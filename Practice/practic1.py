# name = input("Input your name: ")
# surname = input("Input you Surname: ")
# dateOfBirthday = input("Input date of birthday: ")
# placeOfBirthday = input("Input you place of Birthday: ")
# yearOfBirth = int(input("Input your birth year: "))
# currentYear = int(input("Input what year: "))
# print(name, surname)
# print(dateOfBirthday + "," + " from " + placeOfBirthday)
# print(currentYear - yearOfBirth, "years old. ")


# a = int(input("enter value 1: "))
# b = int(input("enter value 2: "))
# print(a, "+" ,b, "=", a + b)


# DIALOGS WITH ROBOT PYTHON
# say_hello = "Robot:\tHello, my name is Python "
# print(say_hello)
# robot_question1 = "Robot:\tWhat is your name?"
# print(robot_question1)
# user_answer1 = "User:\t"
# robot_question = "\tHow old are you"
# print("Robot:", robot_question + ",", input(user_answer1) + "?")
# user_answer2 = int(input("User:\t"))
# current_year = "2022"
# robot_answer = "Robot:\tSo, you birt in:"
# print(robot_answer, int(current_year) - user_answer2, "?")
# user_answer3 = input("User:\t")
# robot_answer = "Robot:\tExcellent"
# print(robot_answer)
# robot_answer = "Robot:\tSo my calculation are correct :-)"
# print(robot_answer)
#
# robot = "Robot:\tlet's play a little"
# print(robot)
# robot1 = "Robot:\tyou say, you:"
# print(robot1, user_answer2)
# robot2 = "Robot:\tlets calculate, enter any number below"
# print(robot2)
# user_answer4 = input("User:\t")
# print("Robot:\t"+user_answer4, "-", user_answer2, "=",
#       int(user_answer4) - int(user_answer2), ";)")
# robot3 = "Robot:\tEnter the names of any countries " \
#          "in the world, and I will tell you how many regions there are in " \
#          "this country"
# print(robot3)
# countries = input("User:\t")
# if countries == "Ukraine":
#     print("Robot:\t" + countries + ",", "Have 24 regions.")
# elif countries == "Italy":
#     print("Robot:\t" + countries + ",", "Have 20 regions.")
# else:
#     print("Robot:\tNo recognise you countries, please enter again"


#PRACTIC IF, ElIF, ELSE,
# a = ["USA", "UK", "Italy", "Ukraine"]
#
# q = input("Введіть країну: ")
# if q in a:
#     print(True)
# else:
#     print(False)

# EXAMPLE CYCLE ON PYTON
# while True:
#     countries = input("User:\t")
#     if countries == "Ukraine":
#         print("Robot:\t" + countries + ",", "Have 24 regions.")
#         break
#     elif countries == "Italy":
#         print("Robot:\t" + countries + ",", "Have 20 regions.")
#         break
#     else:
#         print("Robot:\tNo recognise you countries, please enter again")
#         continue

# n1 = input("1: ")
# n2 = bool(input("2: "))
# print("1", n1, type(n1))
# print("2", n2, type(n2))


# name = input("Enter you name: ")
# last_name = input("Enter your last name: ")
# age = int(input("Enter your year of birth: "))
# is_married = bool(input("Enter you married: "))
#
# if (2022 - age) >= 18:
#     print(name, last_name, "can get driver license")
# else:
#     print(name, last_name, "don't cant get drive license")


# a = int(input("Please enter minimum sleep hours: "))
# b = int(input("Please enter maximum sleep hours: "))
# h = int(input("Please enter how many hours you sleep: "))
#
# if h >= a and h <= b:
#     print("Good")
# elif h <= a:
#     print("No good")
# elif h >= b:
#     print("To moutch")


# login_reg = input("Enter you login registration: ")
# age_reg = int(input("Enter you age: "))
#
# if age_reg >= 100:
#     print("Ups), People don't live that long")
# elif age_reg <= 18:
#     print("Sorry you, limit age registration Only Adult")
# elif age_reg >= 18 or age_reg <= 100:
#     password_reg = input("Enter you password registration: ")
#     print("Registration complete,", login_reg + ".")
#     password_login = input("Enter you password again to login: ")
#     if password_login == password_reg:
#         print("Welcome to my World", login_reg + ", my Congratulation, Keep Learn")
#     elif password_login != password_reg:
#         print("Finito La Komedia, Good bye", login_reg + ":>)")
#     else:
#         print("Login error")
# else:
#     print("Incorrect age")


# x = int(input("Enter how long you sleep: "))
# y = int(input("Enter you day time sleep: "))
# print(x * 60 + y)


# m = int(input("Enter you optimal time sleep:  "))
# print(m // 60)
# print(m % 60)


# a = float(input("Please enter first number: "))
# b = float(input("Please enter second number: "))
# operation = input("Please enter you operation: ")
#
# if operation == "+":
#     print(a + b)
# elif operation == "-":
#     print(a - b)
# elif operation == "/":
#     if b == 0:
#         print("Dilennia na nul")
#     else:
#         print(a / b)
# elif operation == "*":
#     print(a * b)
# elif operation == "mod":
#     if b == 0:
#         print("Dilennia na nul")
#     else:
#         print(a % b)
# elif operation == "pow":
#     print(a ** b)
# elif operation == "div":
#     if b == 0:
#         print("Dilennia na nul")
#     else:
#         print(a // b)


# currency = input("Please enter, with currency you need exchange: ")
#
# if currency == "$":
#     rates = float(input("Please enter rate of $, against the hryvnia: "))
#     money = float(input("Please how many $ you need exchange: "))
#     print("You got:", rates * money, "UAH")
# elif currency == "British Pound":
#     rates = float(input("Please enter rate of  British Pound, against hryvnia: "))
#     money = float(input("Please how many British Pound you need exchange: "))
#     print("You got:", rates * money, "UAH")
# elif currency == "Euro":
#     rates = float(input("Please enter rate of Euro, against the hryvnia: "))
#     money = float(input("Please how many Euro you need exchange: "))
#     print("You got:", rates * money, "UAH")


# name = "Oleksandr"
# last_name = "Polishchuk"
# nickname = "AlaNick"
# email = "oleksandr.polishchuk@icloud.com"
# password1 = "1234"
# password2 = "1234"
#
# finally_name = input("Enter you name: ")
# finally_last_name = input("Enter you last name: ")
# finally_nickname = input("Enter you nickname: ")
# finally_email = input("Enter you email: ")
# finally_password1 = input("Enter you password1: ")
# finally_password2 = input("Enter you password2: ")
#
# if (finally_name == name and finally_last_name == last_name and finally_nickname == nickname
#     and finally_email == email and finally_password1 == password1
#     and finally_password2 == password2 and
#     password1 == password2):
#     print("Authorisation complete")

































