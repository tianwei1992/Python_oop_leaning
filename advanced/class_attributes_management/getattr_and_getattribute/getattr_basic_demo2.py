"""访问已存在的属性，不会触发getattr"""
class ClassA:
    _x = 'a'
    def __init__(self, y):
        self._y = y
    def __getattr__(self, item):
        if item == "_z":
        # return '__getattr__'
            return self._x
if __name__ == '__main__':
    a = ClassA("b")
    print(hasattr(a, "_x"))
    # 如过这里是getattributes而不是getattr，那么直接写a._x会引发getattributes无穷递归，因为getattibutes不会放过已经定义过额属性。这里这么写效果上是等效的，但是不会去触发调用__setattr__
    print(object.__getattribute__(a, "_x"))

    # 访问已存在的属性，无论是实例属性还是类属性，都不会调用__getattr__方法
    print(a._x)    # 输出结果 a
    print(a._y)    # 输出结果 b
    # 访问实例不存在的实例属性时,会调用__getattr__方法
    print(a.z)    # 输出结果 __getattr__