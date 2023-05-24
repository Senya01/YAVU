import queries
from http.server import HTTPServer, CGIHTTPRequestHandler
from cgibin.DBconn import con


def main():
    check_all_tables_exist()
    create_all_view()

    # run_server()


def check_all_tables_exist():
    # Проверка наличия таблиц и создание при отсутствии
    for table in [
        ["category", queries.create_category_table_query, queries.insert_category_data_query],
        ["pets", queries.create_pets_table_query, queries.insert_pets_data_query],
        ["customer", queries.create_customer_table_query, queries.insert_customer_data_query],
        ["cheque", queries.create_cheque_table_query, queries.insert_cheque_data_query],
        ["basket", queries.create_basket_table_query, queries.insert_basket_data_query],
        ["sales", queries.create_sales_table_query, queries.insert_sales_data_query],
    ]:
        if not check_table_exist(table[0]):
            create_table_and_fill(table[0], table[1], table[2])


def create_all_view():
    for view in [
        ["pets_by_category", queries.create_view_pets_by_category],
        ["cheques_and_customers", queries.create_view_cheques_and_customers],
        ["most_expensive_pet", queries.create_view_most_expensive_pet],
        ["category_with_most_pets", queries.create_view_category_with_most_pets]
    ]:
        if not check_table_exist(view[0]):
            create_view(view[0], view[1])


def run_server():
    # Запуск веб сервера
    server_address = ("", 8000)
    print("Сервер запущен по адресу http://localhost:8000/")
    httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
    httpd.serve_forever()


def check_table_exist(name):
    connection = con()

    with connection.cursor() as cursor:
        check_table_query = f"SHOW TABLES LIKE '{name}'"
        cursor.execute(check_table_query)
        result = cursor.fetchone()

        return result


def create_table_and_fill(name, create_table_query, insert_data_query):
    connection = con()
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)
        cursor.execute(insert_data_query)
        connection.commit()

    print(f"Table {name} have been created and filled.")


def create_view(name, create_view_query):
    connection = con()
    with connection.cursor() as cursor:
        cursor.execute(create_view_query)
        connection.commit()

    print(f"View {name} have been created.")


if __name__ == '__main__':
    main()
