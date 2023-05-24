#!/usr/bin/env python3
from DBconn import con
import cgi
import html


# Запись изображений в файл
def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)


form = cgi.FieldStorage()
name = form.getfirst("name", "постое значение")
email = form.getfirst("email", "постое значение")
passw = form.getfirst("pass", "пустое значение")
cat_yes = form.getfirst("cat_yes", "пустое значение")
dog_yes = form.getfirst("dog_yes", "пустое значение")
choose = form.getfirst("choose", "пустое значение")

name = html.escape(name)
email = html.escape(email)
passw = html.escape(passw)
cat_yes = html.escape(cat_yes)
dog_yes = html.escape(dog_yes)
choose = html.escape(choose)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
       <html>
       <head>
           <meta charset="utf-8">
           <title>Обработка данных форм</title>
           <link rel="stylesheet" href="../style.css">
       </head>
       <body id='cats'>""")
# Вывод полученных значений
print("<h4>Рады видеть Вас, {}!</h4>".format(name))
print("<p>Почта: {}</p>".format(email))
print("<p>Пароль: {}</p>".format(passw))
print("<p>Наличие кота: {}</p>".format(cat_yes))
print("<p>Наличие собаки: {}</p>".format(dog_yes))
print("<p>Пожелания: {}</p>".format(choose))

# Если стоят две галочки
if cat_yes == "cat" and dog_yes == "dog":
    print("<img src='../img/cat_or_dog.jpg' class='displayed'> </h4>")
    print("<h4>Рады видеть Вас, {}! Вам надо определиться КОТА или СОБАКУ</h4>".format(name))
    print("""</body>
           </html>""")
# Если хотят купить кота
elif cat_yes == "cat":
    print("<img src='../img/cats1.avif' class='displayed'> </h4>")
    print("<h2>Рады видеть Вас, {}! Выберите себе КОТА:</h2> "
          "<form action='shop.py'>".format(name))
    with con() as cur:
        vh = f"SELECT * FROM `pets`;"
        cur.execute(vh)
        res = cur.fetchall()
        for i in res:
            print(f"<div class='cart'><b>Кличка - </b>{i['name_pet']}, <b>цена - </b>{i['price']}р.")
            img = i['img_pet']
            # Вызов функции записи изображения в файл
            write_file(img, f"{i['name_pet']}.jpg")
            # open(f"{i['name_pet']}.jpg", 'wb').write(i['img_pet'])
            print(f"<img src='../{i['name_pet']}.jpg' class='displayed_pets'>")
            print(f"<b> Подробнее - </b>{i['description']} <hr> "
                  f"<input type='submit' value='Купить >> ' id='it'></div>")
    print("""</form></body> </html>""")

# Если хотят купить собаку
elif dog_yes == "dog":
    print("<img src='../img/dogs.jpg' class='displayed'> </h4>")
    print("<h4>Рады видеть Вас, {}! Выберите себе СОБАКУ:</h4>".format(name))

    print("""</body>
           </html>""")
