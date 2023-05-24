a = 37


def foo():
    print("Функция foo(), a=%s" % a)


def bar():
    print("Функция bar(), вызывается функция foo()")
    foo()


class spam(object):
    def grok(self):
        print("Метод spam.grok")
