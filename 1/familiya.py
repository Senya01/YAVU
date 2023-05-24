from datetime import datetime

year_now = datetime.now()
special = "ИС"


class Student(object):
    def __init__(self, name, sname, lname, group, year_birth):
        self.name = name
        self.sname = sname
        self.lname = lname
        self.group = group
        self.year_birth = year_birth

    def age(self):
        age = year_now.year - self.year_birth
        print(f"Возраст: {age}")

    def fio(self):
        print(f"Имя: {self.name}, Фамилия: {self.sname} , Отчество: {self.lname} , Группа: {self.group}")
        self.age()

    def info(self):
        fio = " ".join([self.name, self.sname, self.lname])
        age = year_now.year - self.year_birth
        print(f"ФИО: {fio}, Возраст: {age}, Группа: {self.group}, Специальность: {special}")
