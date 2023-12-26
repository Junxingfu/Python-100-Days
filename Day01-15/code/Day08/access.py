class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)


"""
test._Test__bar()：调用对象的私有方法 __bar。在Python中，
私有方法可以通过 _ClassName__methodName 的方式访问，
这里 __bar 变成了 _Test__bar。

print(test._Test__foo)：试图访问对象的私有属性 __foo。
同样，私有属性可以通过 _ClassName__attributeName 的方式访问，
这里 __foo 变成了 _Test__foo。
"""

if __name__ == "__main__":
    main()
