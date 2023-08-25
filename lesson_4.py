#Списки - list
#4 str, int, float, bool, list
# print("10" + 5)
# name1 = "Kurmanbek"
# name2 = "Syimyk"
# name3 = "Beksultan"
# name4 = "Nurbolot"
# print(name1, name2, name3, name4)

# names = ["Kurmanbek", "Syimyk", "Beksultan", "Nurbolot"]
# print(names)
# lst = [10, 0.1, "Geeks", False]
# print(lst)

# it = ["Google", "Amazon", "Mad Devs"]
# print(it)
# it.append("GeekStudio") #метод append добавляет в конец списка значение
# print(it)
# it.append("Apple")
# print(it)
# it.remove("Amazon") #метод remove удаляет значение из списка
# print(it)
# # it.remove("Bayas") #Если значение которую нужно удалить в списке нету, то
# #                     #выводится ошибка
# # print(it)

# cars = ["BMW", "Tesla", "BYD", "Mercedes"]
#          #0       1       2        3
# print(cars)
# print(cars[1])
# print(cars[1][2])
# print(cars[1:3]) #В списках можно использовать срезы и индексы
# cars[2] = "Zeekr" #Обновление значение из списка с помощью индексов
# print(cars)
# cars.pop(2) #Метод pop удаляет из списка по индексу
# print(cars)

# numbers = [101, 202, 506, 702, 1001]
# print(numbers)
# numbers.insert(0, "Bayastan") #Метод insert добавляет значение по индексу
# print(numbers)
# del numbers[0:2] #Оператор del удаляет знаение по индексу и срезу
# print(numbers)

# nums = [345, 123, 456, 678, 11, 19, 3]
# nums.sort(reverse=True) #Метод sort, сортирует данные внутри списка
# print(nums)

# lst = ["Geeks", "Hello", "World", "Abc", "Bayas"]
# lst.sort()
# print(lst)

# #Tuple - кортежи
# numbers = ("Asus", "Lenovo", "Apple", "HP", "Acer")
# #Тип данных tuple(кортежи) обозначаются в круглых скобках и являются неизменными
# print(numbers)
# print(numbers.count('Acer'))
# print(numbers.index('Acer'))
# print(numbers[2])
# print(numbers[::-1])
# tup = (10, 3.0, "Hello", True)
# print(tup)

# students = ["Nurbolot", "Bayastan", "Syimyk", "Beksultan", "Janysh"]
# name = input("Имя: ").title()
# if name in students:
#     print(name, "есть в списке")
# else:
#     print("К сожелению такого студента нету в списке")

# import random

# random_number = random.randint(1, 3)
# print(random_number)
# user_number = int(input("Введите число: "))
# if random_number == user_number:
#     print("Победа! Вы выиграли!")
# else:
#     print("К сожелению вы проиграли (")