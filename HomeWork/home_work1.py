# Домашнє завдання:
# 1) Олег дізнався, що замовляючи товар з онлайн сервісу він отримає знижку 15%.
# Описати функцію яка приймає ціну товару та повертає за яку ціну хлопець може купити товар.
#
#
# 2) Описати функцію яка приймає цифри від 1 до 7 і повертає який це день тижня. (Понеділок - Неділя)
# Приклад
# Функція приймає число 3
# Повернення: Середа
#
#
# 3) За контрактом Андрій отримує 2000$ в місяць. Після перегляду контракту його зарплата становить 3500$.
# Описати функції які підраховують річну зарплату в обох випадках.


# Задача №2


# def day_inf():
#     day_list = {
#         1: "Понеділок",
#         2: "Вівторок",
#         3: "Середа",
#         4: "Четвер",
#         5: "Пятниця",
#         6: "Субота",
#         7: "Неділя"
#     }
#
#     while True:
#         a = int(input("Введіть число від 1 до 7: "))
#
#         if a not in day_list:
#             return "Такого числа немає в нашому діапазоні."
#             break
#         else:
#             return "Під номером", a, "День тижня", day_list[a]
#
#
# print(day_inf())


# Задача №3
# firstContract = 2000
#
#
# def salary1_inf():
#     return firstContract * 12
#
#
# def salary2_inf():
#     global firstContract
#     firstContract = 3500
#     return firstContract * 12
#
#
# print(firstContract)
# print(salary1_inf())
# print(salary2_inf())
# print(firstContract)


# value = float(input("Please enter value: "))
# percent = int(input("Enter how many percent you want get: "))
# print((value * percent) / 100)

# Задача 1
# def sell_offer(offer):
#     return (offer * 15) / 100
#
#
# item = float(input("Enter items value: "))
# print(sell_offer(item))


# Задача
# Описати функцію оренди авто яка приймає назву авто, ціну за оренду за годину та кількість бажаних годин оренди.
# Повернути формат "Ціна <назва авто> на <кількість годин> = підрахувати ціну оренди".
# Значення параметрів функціїї приймаються від користувача.

# def rent_car(car, price, time):
#     result = f"Price {car} on {time} hours = {time * price}"
#     return result


# carName = input("Please select model car: ")
# rentPrice = int(input("Enter price per car: "))
# rentTime = float(input("Enter how long you want rent car: "))
# print(rent_car(carName, rentPrice, rentTime))


# Написати функцію яка повертає значення True якщо число входить в проміжок від 0 о 10
# і повертає False якщо число менше 0.


# def number_inf(a):
#     if a >= 0 and a <= 10:
#         return True
#     elif a <= 0:
#         return False
#
#
# b = int(input("Enter number: "))
# print(number_inf(b))


# Написати функцію яка приймає параметрами по стандарту age and name і задає їм стандартні
# значення age = 18, name = Vasil в функції за бажанням користувач має можливість змінити значення змінних або вивести
# результат з значеннями по стандарту.


# def people_inf(age=18, name="Vasil"):
#     question = input("Enter question: ")
#     if question == "yes":
#         age = int(input("Change age: "))
#         name = input("Change name: ")
#         return age, name
#     else:
#         return age, name
#
#
# print(people_inf())


# Описати функцію яка обчислує скільки років потрібно людині для виходу на пенсію. Якщо пенсійний вік = 65 років.


# def old_people(age):
#     return 65 - age
#
#
# print(old_people(30))


# Ціна оренди квартири становить 8000 за місяць але після зміни контракту ціна встановлена на рівні 12000,
# описати функціїї які обчислють плату за рік в обох випадках.


# rentFlat = 8000
#
#
# def rent_info():
#     return rentFlat * 12
#
#
# def rent2_info():
#     global rentFlat
#     rentFlat = 12000
#     return rentFlat * 12
#
#
# print(rent_info())
# print(rent2_info())


# Описати функцію яка приймає слово і максимальну кількість дозволених літер в слові. Якщо слово проходить валідацію
# (кількість букс в слові < максимальна кількість букв) то повертається значення True а в іншому випадку значення False.


# def word_inf(word, wordmax):
#     if len(word) < wordmax:
#         return True
#     else:
#         return False
#
#
# print(word_inf("name", 3))

