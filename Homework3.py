#6
#from random import *
#nimekirja=[]
#N=int(input("Sisesta numbrite pikkus: "))
#for i in range(N):
#    arv=randint(10,100)
#    nimekirja.append[arv]
#maksimum=nimekirja[0]
#max
#for i in range(len(nimekirja)):
#    if nimekirja[i]==maksimum:
#        nimekirja[i]=useless_number
#print("Esialgne nimekiri: "+str(nimekirja))
#print()

#from random import *
#from string import *
#numbers = input("Введите числа через пробел: ").split()
#numbers = list(map(int,numbers))
#if not numbers:
#    print("Ошибка:список чисел пуст.")
#else:
#    max_numbers = max(numbers)
#numbers[numbers.index(max_number)] = max_number / len(numbers)
#print("")

#7
#from random import *
#numbers = sorted([random.randint(-100, 100) for _ in range(6)], key=abs, reverse=input("Kas soovite sorteerida kahanevas (k) või kasvavas (v) järjekorras? ").lower() == "k")
#print("Sorteeritud nimekiri:")
#print(*numbers, sep="\n")


#8
#lists = [
#    ['крот', 'белка', 'выхухоль'],
#    ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],
#    ['qweasdqweas', 'q', 'rteww', 'ewqqqqq']
#]
#max_length = 0
#for sublist in lists:
#    for string in sublist:
#        if len(string) > max_length:
#            max_length = len(string)
#for sublist in lists:
#    for i in range(len(sublist)):
#        sublist[i] = sublist[i].ljust(max_length, '_')
#for sublist in lists:
#    print(sublist)
#9
#name = input("Введите ваше имя: ")
#if not name.isalpha():
#    print("Имя должно содержать только буквы.")
#    exit()
#print("Привет,", name.capitalize())
#total_letters = len(name)
#vowels = sum(1 for letter in name if letter.lower() in 'aeiouаеёиоуыэюя')
#consonants = total_letters - vowels
#print("Количество букв в имени:", total_letters)
#print("Количество гласных букв:", vowels)
#print("Количество согласных букв:", consonants)
#print("Буквы в имени в алфавитном порядке:", *sorted(set(name.lower())))
12
from random import * 
numbers = [random.randint(1, 100) for _ in range(10)]
print("Исходный список:", numbers)
min_number = min(numbers)
max_number = max(numbers)
min_index = numbers.index(min_number)
max_index = numbers.index(max_number)
numbers[min_index] = max_number
numbers[max_index] = min_number
print("Список после замены минимального и максимального элементов:", numbers)


