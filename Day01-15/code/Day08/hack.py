"""
另一种创建类的方式

Version: 0.1
Author: 骆昊
Date: 2018-03-08
"""


def bar(self, name):
    self._name = name


def foo(self, course_name):
    print('%s正在学习%s.' % (self._name, course_name))


def main():
    Student = type('Student', (object,), dict(__init__=bar, study=foo))
    stu1 = Student('骆昊')
    stu1.study('Python程序设计')


if __name__ == '__main__':
    main()  
"""
 (object,) 中的逗号是为了确保 bases 参数被正确解释为一个元组，即使它只有一个元素
 type 是一个元类（metaclass），除了可以返回对象的类型外，它还可以用于动态地创建类。通过 type 可以创建一个新的类，这个过程类似于使用 class 关键字定义类。


type 函数的基本语法如下：
type(name, bases, dict)
name：类的名称。
bases：基类（父类）的元组。
dict：类的字典，包含类的属性和方法。
在你提供的代码中，使用 type 动态创建了一个类 Student，其基类是 object，并且包含 __init__ 方法和 study 方法。这个创建类的过程等价于使用 class 关键字的方式，只不过使用了更底层的 type 功能。

具体来说，下面是代码中使用 type 创建类的部分：
Student = type('Student', (object,), dict(__init__=bar, study=foo))
这一行代码的作用是创建了一个名为 Student 的类，它继承自 object，并拥有 __init__ 和 study 两个方法。bar 函数被赋予了 __init__ 方法的实现，而 foo 函数被赋予了 study 方法的实现。
"""