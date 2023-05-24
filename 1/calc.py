import workers as w


def request_info():
    post = input("Выберите должность - ")
    if post not in w.worker:
        print("Такой должности не существует")
    else:
        idx = w.worker.index(post)
        if idx == 0 or 3:
            priz = w.priz[2]
        elif idx == 2:
            priz = w.priz[1]
        else:
            priz = w.priz[0]
        print(f"Вам положена премия {priz}% от оклада")

        salary = int(input("Введите размер оклада - "))
        print(f"Ваш оклад с премией равен - {salary * (100 + priz) / 100}")

        car = input("Введите 1 если у вас есть автомобиль и 0 если нет - ")

        if car == 1:
            print("Вам не положен проездной!")
        else:
            print("Вам положен проездной!")


if __name__ == '__main__':
    request_info()
