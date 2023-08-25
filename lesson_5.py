#Циклы for и while
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# for number in range(1001):
#     print(number)

# for num in range(10, 21, 2): #в циклах с использованием функции range, 
#                                 #можно указывать начало, конец и шаг
#     print(num) #выводим временную переменную num

# numbers = [] #создаем пустой список numbers
# for i in range(1, 100, 2): #Создаем цикл for, с использованием range
#     numbers.append(i) #С каждым циклом(повтором) добавляем числа в список
# print(numbers) #Выводим результат(список)

# names = ["Bayastan", "Nurbolot", "Janysh", "Beka", "Islam"]
# print(names)
# for name in names:
#     print("Привет", name)

# nums = [101, 3, 441, 1002, 4, 5, 13, 321, 777, 888, 907, 902, 102, 54]
# for num in nums:
#     if num % 2 == 0:
#         print(num, "четный")
#     else:
#         print(num, "нечетный")

#Цикл while
# num1 = 10
# num2 = 20
# while num2 > num1:
#     num1 += 1
#     # num1 = num1 + 1
#     print(num1)

n = 0 #Создаем переменную n для подсчета кругов цикла, по умолчанию равен 0
while True: #Создаем бесконечный цикл с помощью while True
    n += 1 #С каждым циклом(повтором) добавляем в нашу переменную цифру 1
    print(n, "Hello Geeks") #Выводим количество повторов с Hello Geeks
    # if n == 10000: #Делаем условие в котором если число равен 10000
    #     print("STOP") #Выводим слово STOP
    #     break #Досрочно заканчиваем цикл с помощью оператора break
    if n == 10000:
        print("HELLO")
        continue