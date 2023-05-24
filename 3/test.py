import pymysql
from config import host, user, password, db_name


def main():
    # Часть 1
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print('Successfully connected...')
        print("=" * 20)

        # Часть 2
        # ЗАДАНИЕ 1
        new_db_name = input("Введите имя для новой базы данных: ")
        create_db_query = f"CREATE DATABASE {new_db_name}"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
        print(f"База данных '{new_db_name}' успешно создана.")

        # ЗАДАНИЕ 2
        delete_db_name = input("Введите имя базы данных для удаления: ")
        delete_db_query = f"DROP DATABASE {delete_db_name}"
        with connection.cursor() as cursor:
            cursor.execute(delete_db_query)
        print(f"База данных '{delete_db_name}' успешно удалена.")

        # ЗАДАНИЕ 3
        show_databases_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            cursor.execute(show_databases_query)
            rows = cursor.fetchall()
            print("Список баз данных:")
            for row in rows:
                print(row["Database"])
            print(f"Количество баз данных: {len(rows)}")

        # Часть 3
        # Задание 1:
        create_db_query = "CREATE DATABASE KMPO"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
        print("База данных KMPO успешно создана.")

        # Создание таблицы spec
        create_spec_table_query = """
        CREATE TABLE KMPO.spec (
            id INT(11) NOT NULL AUTO_INCREMENT,
            name VARCHAR(50) NOT NULL,
            PRIMARY KEY (id)
        )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_spec_table_query)
        print("Таблица spec успешно создана.")

        # Создание таблицы students
        create_students_table_query = """
        CREATE TABLE KMPO.students (
            id INT(11) NOT NULL AUTO_INCREMENT,
            name VARCHAR(50) NOT NULL,
            spec_id INT(11) NOT NULL,
            PRIMARY KEY (id),
            FOREIGN KEY (spec_id) REFERENCES spec(id)
        )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_students_table_query)
        print("Таблица students успешно создана.")

        # Задание 2
        create_user1_query = "CREATE USER 'user1'@'localhost' IDENTIFIED BY 'password1'"
        with connection.cursor() as cursor:
            cursor.execute(create_user1_query)
        print("Пользователь user1 успешно создан.")

        grant_privileges_query = "GRANT ALL PRIVILEGES ON KMPO.* TO 'user1'@'localhost' WITH GRANT OPTION"
        with connection.cursor() as cursor:
            cursor.execute(grant_privileges_query)
        print("Привилегии назначены пользователю user1.")

        # Задание 3
        create_user2_query = "CREATE USER 'user2'@'localhost' IDENTIFIED BY 'password2'"
        with connection.cursor() as cursor:
            cursor.execute(create_user2_query)
        print("Пользователь user2 успешно создан.")

        grant_select_update_query = "GRANT SELECT, UPDATE ON KMPO.spec TO 'user2'@'localhost'"
        with connection.cursor() as cursor:
            cursor.execute(grant_select_update_query)
        print("Привилегии назначены пользователю user2.")

        # Задание 4
        grant_delete_query = "GRANT DELETE ON KMPO.* TO 'user2'@'localhost'"
        with connection.cursor() as cursor:
            cursor.execute(grant_delete_query)
        print("Привилегии на удаление таблиц назначены пользователю user2.")

        # Задание 5
        revoke_privileges_query = "REVOKE ALL PRIVILEGES ON KMPO.* FROM 'user1'@'localhost'"
        with connection.cursor() as cursor:
            cursor.execute(revoke_privileges_query)
        print("Привилегии отозваны у пользователя user1.")

        # Задание 6
        delete_user1_query = "DROP USER 'user1'@'localhost'"
        with connection.cursor() as cursor:
            cursor.execute(delete_user1_query)
        print("Пользователь user1 удален.")

        # Задание 7
        grant_super_query = "GRANT ALL PRIVILEGES ON *.* TO 'user2'@'localhost' WITH GRANT OPTION"
        with connection.cursor() as cursor:
            cursor.execute(grant_super_query)
        print("Пользователь user2 назначен суперпользователем.")

    except Exception as ex:
        print('Connection refused...')
        print(ex)


if __name__ == '__main__':
    main()
