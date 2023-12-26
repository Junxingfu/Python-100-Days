"""
练习
修一个游泳池 半径(以米为单位)在程序运行时输入 游泳池外修一条3米宽的过道
过道的外侧修一圈围墙 已知过道的造价为25元每平米 围墙的造价为32.5元每米
输出围墙和过道的总造价分别是多少钱(精确到小数点后2位)

Version: 0.1
Author: 骆昊
Date: 2018-03-08
"""

import math


"""
@property：
只读属性： 使用 @property 装饰的方法可以像访问属性一样被访问，但不能被修改。在这个例子中，外部代码可以通过 circle.radius 来访问半径值，但不能通过 circle.radius = new_radius 来修改半径值。

封装实现细节： 将属性的获取方法封装在 @property 装饰的方法中，可以在后续修改类的内部实现而不影响外部代码。如果未来需要添加一些额外的逻辑来计算半径，只需修改 radius 方法而不需要改变外部代码。

属性名和方法名一致： 使用 @property 装饰器可以使属性名和方法名保持一致，提高代码的可读性。在这个例子中，半径的获取通过 circle.radius 而不是 circle.get_radius()。
"""
class Circle(object):

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius if radius > 0 else 0

    @property
    def perimeter(self):
        return 2 * math.pi * self._radius

    @property
    def area(self):
        return math.pi * self._radius * self._radius


if __name__ == '__main__':
    radius = float(input('请输入游泳池的半径: '))
    small = Circle(radius)
    big = Circle(radius + 3)
    print('围墙的造价为: ￥%.1f元' % (big.perimeter * 115))
    print('过道的造价为: ￥%.1f元' % ((big.area - small.area) * 65))
