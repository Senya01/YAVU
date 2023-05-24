def division():
    try:
        num1 = float(input("Введите число 1: "))
        num2 = float(input("Введите число 2: "))

        quotient = num1 / num2
        difference = abs(num1 - num2)

        print("Частное:", quotient)
        print("Разность:", difference)

    except ValueError:
        print("Ошибка: Введено недопустимое значение!")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль!")
