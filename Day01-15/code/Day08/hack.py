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

"""
The first argument to type is the name of the class, which is 'Student' in this case.

The second argument is a tuple of base classes. 
In this case, there's only one base class, which is object.

The third argument is a dictionary that defines the attributes and methods of the class. 
It includes __init__ and study methods.
"""
if __name__ == '__main__':
    main()  
