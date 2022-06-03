# Spysok (list) - typ dannych


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


peoples = ["Oleksandr", "Alan"]
print(peoples)
peoples.append("Serhii")  # Метод append - добавляє елемент в кінець листа.
print(peoples)
peoples.insert(1, "Alanik")  # Метол inser - добавляє елемент по індексу.
print(peoples)
peoples.extend([1, 2, 3])  # Метод extend - розширює  елементи в (list)
print(peoples)
print(peoples.index("Serhii"), peoples.index("Alanik"))  # Метод index - показує під яким індексом
                                                         # знаходиться певний елементю.
peoples.pop(3)
print(peoples)  # Метод pop - видаляє елементи листа по індексу.
peoples.remove(1)  # Метод remove - видаляє по значенню.
print(peoples)
peoples.clear()  # Метод clear - видаляє всі елементи з (list)
print(peoples)
















