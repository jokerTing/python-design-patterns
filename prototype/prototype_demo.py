import sys
import copy

class Point:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y

def make_object(Class, *args, **kwargs):
    return Class(*args, **kwargs)

# 传统静态方式 Ponit当作构建器来使用
point1 = Point(1, 2)
# 把类名当成参数传给相关函数
point2 = eval("{}({}, {})".format("Point", 2, 4)) 
point3 = getattr(sys.modules[__name__], "Point")(3, 6)
point4 = globals()["Point"](4, 8)# 使用内置的globals 更优雅
# 通用函数
point5 = make_object(Point, 5, 10)
# 经典原型方式
# 根据现有对象复制出新对象
point6 = copy.deepcopy(point5)
point6.x = 6
point6.y = 12
# 效率更高的原型方法
# 无需先克隆，直接用新参数创建新对象
point7 = point1.__class__(7, 14)