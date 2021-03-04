# 装饰器的使用
def can_play(fn):
    def inner(x, y, *args, **kwargs):
        if args[0] <= 22:
            fn(x, y)
        else:
            print("太晚了，早点睡吧~")

    return inner


@can_play
def play_game(name, game):
    print("{}正在玩{}".format(name, game))


play_game("张三", "王者荣耀", 19)
play_game("李四", "绝地求生", 23)
