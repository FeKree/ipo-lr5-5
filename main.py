sogl = "бвгджзйклмнпрстфхцчшщ" #Строка со списком согласных букв
str1 = input("Введите предложение: ") #Вводим строку с которой будут происходить действия
Ilist = [] #Создаем список где будут храниться индексы
for i in range(len(str1)): #Условие цикла где будут через длину введеной строки перебираться символы и искаться согласные
    if str1[i] in sogl: #Ветвление где проверяется через индекс со списка будут в 6 строке заполнятся
        Ilist.append(i) #Через цикл заполняем список 
print("Индексы согласных букв будут: ") #Выводим индексы