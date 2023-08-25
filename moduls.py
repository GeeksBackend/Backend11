#Модули
#1 - импортировать сам модуль
# import lesson_8 #без окончания .py

# lesson_8.welcome('Baiastan') #Вызываем функцию welcome, из модуля lesson_8.py
# lesson_8.add(100, 34)

#2 - импортировать отдельные определения из модуля
# from lesson_8 import welcome, add

# welcome('Beksultan')
# add(200, 1234)

#3 - импортировать всё содержимое модуля сразу
from lesson_8 import *

welcome('Nurbolot')
add(333, 345)