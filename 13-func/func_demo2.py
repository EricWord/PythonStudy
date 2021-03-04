def add(a, b, *args,mul=1,**kwargs):
    '''

    :param a:
    :param b:
    :param args: 可变位置参数
    :param mul:
    :param kwargs:可变的关键字参数，以字典的形式保存
    :return:
    '''
    return a + b


add(1, 2, 3, 4, 5, 6)
