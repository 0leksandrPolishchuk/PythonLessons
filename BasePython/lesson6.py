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


def calc_result(a, b, c):
    # print("a:", a)
    # print("b:", b)
    # print("c:", c)
    print(a + b - c)


while True:
    result_a = float(input("enter value <a> : "))
    result_b = float(input("enter value <b> : "))
    result_c = float(input("enter value <c> : "))
    calc_result(result_a, result_b, result_c)


