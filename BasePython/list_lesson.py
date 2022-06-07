# Список (list) - тип данних.


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# print(numbers)
# print(type(numbers))


# peoples = ["Alex", "Serhii", "Alan", "Danik", "Emma"]
# print(peoples)
# print(type(peoples))


# objects = [1, True, False, 2.1, "Years", [1]]
# print(objects)
# print(type(objects))
#
# for i in objects:
#     print(i)


# numbers1 = []
# numbers2 = list()
# print(numbers1, numbers2)


# x = list([1, 2, 3, 4, 5])
# print(x)


# numbers = [5] * 5
# print(numbers)


# people = ["Alan", "Agnieszka"] * 3
# print(people)
#
# for i in people:
#     print(i)


# objects = [1, "London", "Ukraine", 10.10, "Laptop", True, False]
# print(objects)
# print(objects[1])
# print(objects[6])
# print(objects[-1])


# objects = [1, "London", "Ukraine", 10.10, "Laptop", True, False]
# print(objects)
# objects[0] = 5
# print(objects)
# objects[-4] = 7
# print(objects)


# peoples = ["Danik", "Alex", "Emma"]
# name1, name2, name3 = peoples
# print(name1, name2, name3)
# print(name2)
# print(name3)


# peoples = ["Danik", "Alex", "Emma", "John", "Travolta", "Terminator", "Robokop", "Batmen"]
# while True:
#     questions = int(input("Please enter index elements: "))
#     print(peoples[questions])


# numbers = [50, 80, 34, 67, 90]
# counter = 0
# while counter < len(numbers):
#     print(numbers[counter])
#     counter += 1


# a = input("Enter you name: ")
# print(a)
# print(len(a))


# peoples = ["Danik", "Alex", "Emma", "John", "Travolta", "Terminator", "Robokop", "Batmen"]
# print(peoples)
# print(len(peoples))
# for i in peoples:
#     print(i, "len:", len(i))


# peoples = ["Oleksandr", "Alan"]
# print(peoples)
# peoples.append("Serhii")  # Метод append - добавляє елемент в кінець листа.
# print(peoples)
# peoples.insert(1, "Alanik")  # Метод insert - добавляє елемент по індексу.
# print(peoples)
# peoples.extend([1, 2, 3])  # Метод extend - розширює  елементи в (list)
# print(peoples)
# print(peoples.index("Serhii"), peoples.index("Alanik"))  # Метод index - показує під яким індексом
                                                         # знаходиться певний елемент.
# peoples.pop(3)  # Метод pop - видаляє елементи листа по індексу.
# print(peoples)
# peoples.remove(1)  # Метод remove - видаляє по значенню.
# print(peoples)
# peoples.clear()  # Метод clear - видаляє всі елементи з (list)
# print(peoples)


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

# users = [
#     ["Oleksandr", 37, 1985],
#     ["Inna", 38],
#     ["Emma", 9]
# ]
# print(users)
# print(users[-1][0])
# print(users[1][0])
# print(users[0][2])