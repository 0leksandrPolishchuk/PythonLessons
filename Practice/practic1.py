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
say_hello = "Robot:\tHello, my name is Python "
print(say_hello)
robot_question1 = "Robot:\tWhat is your name?"
print(robot_question1)
user_answer1 = "User:\t"
robot_question = "\tHow old are you"
print("Robot:", robot_question + ",", input(user_answer1) + "?")
user_answer2 = int(input("User:\t"))
current_year = "2022"
robot_answer = "Robot:\tSo, you birt in:"
print(robot_answer, int(current_year) - user_answer2, "?")
user_answer3 = input("User:\t")
robot_answer = "Robot:\tExcellent"
print(robot_answer)
robot_answer = "Robot:\tSo my calculation are correct :-)"
print(robot_answer)

robot = "Robot:\tlet's play a little"
print(robot)
robot1 = "Robot:\tyou say, you:"
print(robot1, user_answer2)
robot2 = "Robot:\tlets calculate, enter any number below"
print(robot2)
user_answer4 = input("User:\t")
print("Robot:\t"+user_answer4, "-", user_answer2, "=",
      int(user_answer4) - int(user_answer2), ";)")
