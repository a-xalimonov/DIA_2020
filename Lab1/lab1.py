import math

#Ввод значений
def mainInput():
    while True:
        try:
            return map(int,input().split())
        except ValueError:
            print("Введёны некорректные значения. Повторите ввод.")

#Дискриминант
def discr(a, b, c):
    return b ** 2 - 4 * a * c

#Вывод результата
def printResult(resultList):
    for i in range(len(resultList)):
        print("x" + str(i) + " = " + str(resultList[i]))

print("Халимонов Антон, группа ИУ5-53Б")

a, b, c = mainInput()
D = discr(a, b, c)

if D < 0:
    print("Действительных корней нет")
else:
    

    t1 = (-b - math.sqrt(D)) / (2 * a)
    t2 = (-b + math.sqrt(D)) / (2 * a)

    resultList = []
    resultList.append(math.sqrt(t1))
    resultList.append(-math.sqrt(t1))
    resultList.append(math.sqrt(t2))
    resultList.append(-math.sqrt(t2))

    printResult(resultList)
    
input()