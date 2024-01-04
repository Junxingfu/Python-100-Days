class Apple:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


def test1():
    apple = Apple("one", 1)
    print(apple.name)
    apple.name = "two"
    print(apple.name)


"""
使用 _name 时，如果没有get,set方法，无法直接使用
"""
if __name__ == '__main__':
    test1()
