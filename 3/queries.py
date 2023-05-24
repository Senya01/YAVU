create_category_table_query = """
CREATE TABLE category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(32),
    description VARCHAR(255)
);
"""

create_pets_table_query = """
CREATE TABLE pets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(32),
    nick VARCHAR(32),
    age INT,
    gender VARCHAR(10),
    breed VARCHAR(32),
    price DECIMAL(10, 2),
    img VARCHAR(255),
    description VARCHAR(255),
    id_category INT,
    FOREIGN KEY (id_category) REFERENCES category(id)
);
"""

create_customer_table_query = """
CREATE TABLE customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(32),
    sname VARCHAR(32),
    email VARCHAR(64),
    phone VARCHAR(16),
    passport VARCHAR(16),
    login VARCHAR(32),
    password VARCHAR(32)
);
"""

create_cheque_table_query = """
CREATE TABLE cheque (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE,
    payment_t VARCHAR(32),
    id_customer INT,
    FOREIGN KEY (id_customer) REFERENCES customer(id)
);
"""

create_basket_table_query = """
CREATE TABLE basket (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_customer INT,
    id_pet INT,
    quantity INT,
    FOREIGN KEY (id_customer) REFERENCES customer(id),
    FOREIGN KEY (id_pet) REFERENCES pets(id)
);
"""

create_sales_table_query = """
CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_cheque INT,
    id_pet INT,
    quantity INT,
    FOREIGN KEY (id_cheque) REFERENCES cheque(id),
    FOREIGN KEY (id_pet) REFERENCES pets(id)
);
"""

insert_category_data_query = """
INSERT INTO category (name, description)
VALUES
    ('Category 1', 'Description 1'),
    ('Category 2', 'Description 2'),
    ('Category 3', 'Description 3');
"""

insert_pets_data_query = """
INSERT INTO pets (name, nick, age, gender, breed, price, img, description, id_category)
VALUES
    ('Pet 1', 'Nick 1', 2, 'Male', 'Breed 1', 100.00, 'img1.jpg', 'Description 1', 1),
    ('Pet 2', 'Nick 2', 1, 'Female', 'Breed 2', 150.00, 'img2.jpg', 'Description 2', 2),
    ('Pet 3', 'Nick 3', 3, 'Male', 'Breed 3', 200.00, 'img3.jpg', 'Description 3', 1);
"""

insert_customer_data_query = """
INSERT INTO customer (name, sname, email, phone, passport, login, password)
VALUES
    ('Customer 1', 'Surname 1', 'customer1@example.com', '123456789', 'AB123456', 'customer1', 'password1'),
    ('Customer 2', 'Surname 2', 'customer2@example.com', '987654321', 'CD789012', 'customer2', 'password2');
"""

insert_basket_data_query = """
INSERT INTO basket (id_customer, id_pet, quantity)
VALUES
    (1, 1, 2),
    (1, 2, 1),
    (2, 3, 3);
"""

insert_sales_data_query = """
INSERT INTO sales (id_cheque, id_pet, quantity)
VALUES
    (1, 1, 1),
    (1, 2, 2),
    (2, 3, 1);
"""

insert_cheque_data_query = """
INSERT INTO cheque (data, payment_t, id_customer)
VALUES
    ('2023-05-24', 'Cash', 1),
    ('2023-05-23', 'Credit Card', 2);
"""

# Views
# Запрос 1: Список питомцев по категориям
create_view_pets_by_category = """
CREATE VIEW pets_by_category AS
SELECT category.name AS category_name, pets.name AS pet_name
FROM category
INNER JOIN pets ON category.id = pets.id_category;
"""

# Запрос 2: Список чеков и покупателей, которым они принадлежат
create_view_cheques_and_customers = """
CREATE VIEW cheques_and_customers AS
SELECT cheque.id AS cheque_id, cheque.data, customer.name AS customer_name
FROM cheque
INNER JOIN customer ON cheque.id_customer = customer.id;
"""

# Запрос 3: Данные о самом дорогом питомце
create_view_most_expensive_pet = """
CREATE VIEW most_expensive_pet AS
SELECT *
FROM pets
ORDER BY price DESC
LIMIT 1;
"""

# Запрос 4: Категория с наибольшим количеством питомцев
create_view_category_with_most_pets = """
CREATE VIEW category_with_most_pets AS
SELECT category.name AS category_name, COUNT(pets.id) AS pet_count
FROM category
INNER JOIN pets ON category.id = pets.id_category
GROUP BY category.name
ORDER BY pet_count DESC
LIMIT 1;
"""


# # View login
# # Запрос 1: Проверка пароля/логина
# create_view_login_validation = """
# CREATE VIEW login_validation AS
# SELECT CASE
#          WHEN EXISTS(SELECT * FROM customer WHERE (email = :login OR login = :login) AND password = :password) THEN 1
#          ELSE 0
#        END AS is_valid;
# """
#
# # Запрос 2: Проверка пароля/логина
#
#
# # Запрос 3: Проверка на длину логина, не менее 4 символов, только английские символы
# create_view_registration_login_validation = """
# CREATE VIEW registration_login_validation AS
# SELECT CASE
#          WHEN LENGTH(:login) >= 4 AND :login REGEXP '^[a-zA-Z]+$' THEN 1
#          ELSE 0
#        END AS is_valid;
# """
#
#
# # Запрос 4: Валидация email на соответствие формату Х@X.X
# create_view_registration_email_validation = """
# CREATE VIEW registration_email_validation AS
# SELECT CASE
#          WHEN :email REGEXP '^[^@\s]+@[^@\s]+\.[^@\s]+$' THEN 1
#          ELSE 0
#        END AS is_valid;
# """
#
# # Запрос 5: Проверка на длину пароля, не менее 6 символов,
# # только английские символы, наличие цифр и букв, наличие символа в верхнем регистре
# create_view_registration_password_validation = """
# CREATE VIEW registration_password_validation AS
# SELECT CASE
#          WHEN LENGTH(:password) >= 6 AND :password REGEXP '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$' THEN 1
#          ELSE 0
#        END AS is_valid;
# """
