# 高级装饰器:装饰器函数带参数
def can_play(clock):
    print("最外层函数被调用了，clock={}".format(clock))

    def handle_action(fn):
        def do_action(name, game):
            if clock < 21:
                fn(name, game)
            else:
                print("太晚了，不能玩游戏了")

        return do_action

    return handle_action


@can_play(20)
def play_game(name, game):
    print(name + "正在玩" + game)


play_game("张三", "王者荣耀")
