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
1. 名字重整（Name Mangling）：
在类的外部，可以使用 _类名__私有变量名 的形式来访问私有变量
2.提供公共方法来访问私有变量。
"""
if __name__ == "__main__":
    main()
