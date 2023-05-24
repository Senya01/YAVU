class ErrorLoginchik(Exception):
    pass


class ErrorPassw(Exception):
    pass


def test_login():
    admin_login = "admin"
    admin_password = "password"

    try:
        login = input("Введите логин: ")
        password = input("Введите пароль: ")

        if login != admin_login:
            raise ErrorLoginchik("Ошибка: Неверный логин!")

        if password != admin_password:
            raise ErrorPassw("Ошибка: Неверный пароль!")

        print("Успешная авторизация!")

    except ErrorLoginchik as e:
        print(e)
    except ErrorPassw as e:
        print(e)
