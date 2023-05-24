import spam as sp
import familiya as f


def main():
    # Spam
    print(sp.a)
    sp.foo()
    s = sp.spam()
    s.grok()
    print("=" * 20, "\n")

    # familiya
    student = f.Student("Арсений", "Селин", "Андреевич", "31ИС-20", 2004)
    student.age()
    student.fio()
    student.info()
    print("=" * 20, "\n")
    student2 = f.Student("Артём", "Львов", "Тимурович", "31ИС-22", 2005)
    student2.age()
    student2.fio()
    student2.info()
    print("=" * 20, "\n")


if __name__ == '__main__':
    main()
