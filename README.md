# 个人学习笔记
_参考：《Python学习手册》第六部分 OOP相关_

## 文档结构
1. 两个文件夹，basic和advanced，前者对应27章，后者是更高级的用法

2. basic/
   * classtools.py演示了工具类的定义，比如AttrDisplay类。
   * person.py演示了普通的继承和对工具类的继承。定义Person继承了工具类AttrDisplay，所以可以使用工具；而Manger类又继承自了Person。
   * makedb.py & readdb.py & updatedb.py演示了shelve模块的用法，它们提供了将类的实例对象写入数据库、读取数据库和更新数据库的方法。
   * embedding_based_person.py演示了类的嵌套，不过这并不是好的例子。Mangager本该继承自Person，但在这里另成一类，在自己的方法实现中调用了Person的实现，从而有了类似于Person的样子。
   * specialize.py 演示了扩展父类的集中方法，值得注意的是Provider对抽象超类Super的继承，子类只有实现了抽象超类的某个方法才能被实例化，否则报错。

3. advanced/
   * combination_demo/演示了好的类的嵌套，也叫组合。有Department、Processor、Pizzashop3个组合的例子。
   * delegation_demo/演示了委托，也叫代理。
   * pseudo_private_attributes_demo/演示了类的伪私有属性的用法，解释了为什么需要它
   * bound_or_unbound_mothod_demo/演示了绑定方法和未绑定方法的用法。注意在Python2和3中对未绑定方法是有区别的。另外也演示了Python的各种可调用对象，包括但不限于绑定方法，显示了Python语言的灵活性。


