# 个人学习笔记
_参考：《Python学习手册》第六部分 OOP相关_

## 文档结构
1. 3个文件夹，basic、advanced、about_class_design，basic对应书上27章，about_class_design对应30章，其他类的高级用法大多在advanced里面。

2. basic/
   * classtools.py演示了工具类的定义，比如AttrDisplay类。
   * person.py演示了普通的继承和对工具类的继承。定义Person继承了工具类AttrDisplay，所以可以使用工具；而Manger类又继承自了Person。
   * makedb.py & readdb.py & updatedb.py演示了shelve模块的用法，它们提供了将类的实例对象写入数据库、读取数据库和更新数据库的方法。
   * embedding_based_person.py演示了类的嵌套，不过这并不是好的例子。Mangager本该继承自Person，但在这里另成一类，在自己的方法实现中调用了Person的实现，从而有了类似于Person的样子。
   * specialize.py 演示了扩展父类的集中方法，值得注意的是Provider对抽象超类Super的继承，子类只有实现了抽象超类的某个方法才能被实例化，否则报错。

3. about_class_design/
   * combination_demo/演示了好的类的嵌套，也叫组合。有Department、Processor、Pizzashop3个组合的例子。
   * delegation_demo/演示了委托，也叫代理。
   * pseudo_private_attributes_demo/演示了类的伪私有属性的用法，解释了为什么需要它。
   * bound_or_unbound_mothod_demo/演示了绑定方法和未绑定方法的用法。注意在Python2和3中对未绑定方法是有区别的。另外也演示了Python的各种可调用对象，包括但不限于绑定方法，显示了Python语言的灵活性。
   * mix_in_classes_demo/由简到难演示了3个混合类的定义，然后在textmixin*.py中测试了效果，说明了多继承在应用得当的时候是很有用的工具。
   * factory_demo/演示了最简单的工厂模式，这里仅做了解，书上的篇幅也很短。
   
4. advanced/
   * builtin_class_extending/演示了内置类的两种扩展方式，代理和继承。其中继承之后，可以是简单修改原有类型的行为，也可以增加新的方法，使之成为与原类型差别较大的类型。
   * slots_and_property/演示了在class里面使用slots和property的方法，对于property详细演示了装饰器用法和静态获取属性实现隐式函数调用。
   * staticmehod_and_classmethod/演示了静态方法和类方法实现了超类实例化次数的统计，最后还用类方法实现了从超类到每个子类各自实例化次数的统计。
   * decorator_demo/简单演示了函数装饰器和类装饰器，其中类装饰器部分是以改写staticmehod_and_classmethod/count_instances_for_each_class_with_classmethod作为演示。
   * nester.py 展示的是函数中嵌套类带来的作用域问题，主要是Python2.2以前的问题，Python3也要注意类的方法中是不能直接看到类的其他变量或者方法的，但是可以看到类名，于是需要用self或者类名去找到其他变量或者方法，如果需要的话。
   * class_attributes_management包含了类属性管理的4种办法：
     1. property（在slots_and_property/中已经演示过，这里不再重复）
     2.  descriptor
     3.  __getattr__
     4.  __getattribute__ 
     
     其中前2个是制造某一个特定的属性，而后2个是拦截通用的各种属性，所以在编码时后两者需要考虑的问题更多更广泛。
     - descriptor_demo/ 演示了描述符的基本用法，以及变量的状态分别保存在描述符状态中和实例状态中这两种情况，最后用描述符语法仿写了property，借以理解property可以算是描述符的特殊情况。
     - getattr_and_getattribute/ 演示了__getattr和__getattribute的基本用法，通过两种办法等效地实现一个虚拟属性来展示了两种用法的区别，重点需要关如何避免递归调用(感觉比较复杂)。
     - comparation_with_4_methods_simple/ 通过用4种方法实现同一个任务——添加类的属性，借此巩固了以上4种方法，并展示了彼此的差异。这里需要注意细节。带有improved的是看书后改进的最终版本，不带的是原始版本。
     - comparation_with_4_methods_complex/ 通过用4种方法实现同一个任务，进一步比较4种方式的差异，有比较代码行数和效率问题。这个例子在书上37章的最后。

