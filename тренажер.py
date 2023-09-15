import random

live = 3
while live > 0:
    actions = random.randint(1, 4)
    # Сложение
    if actions == 1:
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        ans = int(input(f'{num1} + {num2} = '))
        if ans == num1 + num2:
            print("Правильно")
        else:
            print("неправильно")
            live -= 1
    # Вычитание
    elif actions == 2:
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        if num1 < num2:
            num1, num2 = num2, num1
        ans = int(input(f'{num1} - {num2} = '))
        if ans == num1 - num2:
            print("Правильно")
        else:
            print("неправильно")
            live -= 1
    # Умножение
    elif actions == 3:
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        ans = int(input(f'{num1} * {num2} = '))
        if ans == num1 * num2:
            print("Правильно")
        else:
            print("неправильно")
            live -= 1
    # Деление
    elif actions == 4:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        ans = int(input(f'{num1 * num2} / {num2} = '))
        if ans == num1:
            print("Правильно")
        else:
            print("неправильно")
            live -= 1
print("ты проиграл")

