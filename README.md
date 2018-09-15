# 个人学习笔记
_参考：《Python学习手册》第六部分 OOP相关_

## 文档结构
1. 两个文件夹，basic和advanced，前者对应27章，后者是更高级的用法

2. basic/
* classtools.py演示了工具类的定义，比如AttrDisplay类。
* person.py演示了普通的继承和对工具类的继承。定义Person继承了工具类AttrDisplay，所以可以使用工具；而Manger类又继承自了Person。
* makedb.py & readdb.py & updatedb.py演示了shelve模块的用法，它们提供了将类的实例对象写入数据库、读取数据库和更新数据库的方法。
* embedding_based_person.py演示了类的嵌套，不过这并不是好的例子。Mangager本该继承自Person，但在这里另成一类，在自己的方法实现中调用了Person的实现，从而有了类似于Person的样子。
* combination.py演示了好的类的嵌套，也叫组合。将Manager和Person都归类于Department
* specialize.py 演示了扩展父类的集中方法，值得注意的是Provider对抽象超类Super的继承，子类只有实现了抽象超类的某个方法才能被实例化，否则报错


