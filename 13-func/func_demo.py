def say_hello(name, age, city="深圳"):
    '''
    say hello
    :param name:
    :param age:
    :param city: 缺省参数，只能放在参数列表中最后一个位置
    :return:
    '''
    print("大家好，我是{},我今年{}岁了，我来自{}".format(name, age, city))


# 如果没有传递缺省参数的值，就是用缺省参数的默认值
say_hello("jack", 19)  # 大家好，我是jack,我今年19岁了，我来自深圳
# 如果传递了缺省参数的值，就是用传进来的值
say_hello("jack", 19, "北京")  # 大家好，我是jack,我今年19岁了，我来自北京
# 可以部分是用变量赋值的形式传参
# 如果同时有位置参数和关键字参数，关键字参数一定要放在位置参数的后面，而且位置参数必须在首位
say_hello("jerry", age=24, city="南京")# 大家好，我是jerry,我今年24岁了，我来自南京
