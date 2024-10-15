first = int(input("Введите ваше число №1: "))
second = int(input("Введите ваше число №2: "))
third = int(input("Введите ваше число №3: "))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)