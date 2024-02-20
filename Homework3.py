#6
# from random import *

# try:
#     nimekirja = []
#     N = int(input("Sisesta numbrite pikkus: "))
#     for i in range(N):
#         arv = randint(10, 100)
#         nimekirja.append(arv)
#     maksimum = max(nimekirja)  
#     for i in range(len(nimekirja)):
#         if nimekirja[i] == maksimum:
#             nimekirja[i] = "useless_number"  
#     print("Esialgne nimekiri: " + str(nimekirja))
    
# except ValueError:
#     print("Palun sisesta korrektne arv.")
#7
# from random import *

# try:
#     sort_order = input("Kas soovite sorteerida kahanevas (k) või kasvavas (v) järjekorras? ").lower()
#     if sort_order not in ['k', 'v']:
#         raise ValueError("Vale sisend. Sisesta 'k' või 'v'.")
#     numbers = sorted([randint(-100, 100) for _ in range(6)], key=abs, reverse=sort_order == "k")
#     print("Sorteeritud nimekiri: ")
#     print(*numbers, sep="\n")

# except ValueError as e:
#     print("Viga: ", e)

#8
# lists = [
#    ['крот', 'белка', 'выхухоль'],
#    ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],
#    ['qweasdqweas', 'q', 'rteww', 'ewqqqqq']
# ]
# try:
#     max_length = 0
#     for sublist in lists:
#         for string in sublist:
#             if len(string) > max_length:
#                 max_length = len(string)
#     for sublist in lists:
#         for i in range(len(sublist)):
#             sublist[i] = sublist[i].ljust(max_length, '_')
#     for sublist in lists:
#         print(sublist)

# except Exception as e:
#     print("An error occurred: ", e)

#9
# try:
#     name = input("Введите ваше имя: ")
#     if not name.isalpha():
#         raise ValueError("Имя должно содержать только буквы.")
#     print("Привет,", name.capitalize())
#     total_letters = len(name)
#     vowels = sum(1 for letter in name if letter.lower() in 'aeiouаеёиоуыэюя')
#     consonants = total_letters - vowels
#     print("Количество букв в имени: ", total_letters)
#     print("Количество гласных букв: ", vowels)
#     print("Количество согласных букв: ", consonants)
#     print("Буквы в имени в алфавитном порядке:", *sorted(set(name.lower())))

# except ValueError as e:
#     print("Ошибка:", e)
# except Exception as e:
#     print("Произошла непредвиденная ошибка:", e)

#12
# try:
#     from random import *
#     
#     numbers = [randint(1, 100) for _ in range(10)]
#     print("Исходный список: ", numbers)
#     min_number = min(numbers)
#     max_number = max(numbers)
#     min_index = numbers.index(min_number)
#     max_index = numbers.index(max_number)
#     numbers[min_index] = max_number
#     numbers[max_index] = min_number
#     print("Список после замены минимального и максимального элементов: ", numbers)

# except Exception as e:
#     print("Произошла ошибка: ", e)



