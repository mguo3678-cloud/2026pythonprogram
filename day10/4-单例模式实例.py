# 作者: 学不会
# 2026年10月15日15时58分51秒
# xxx@qq.com

# a=[1,2,3]
# b=[1,2,3]
# print(a==b)
# print(a is b)
# print(id(a))
# print(id(b))

class MusicPlayer:
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            print("创建对象，分配空间")
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):
        if not MusicPlayer.init_flag:
            MusicPlayer.init_flag = True
            print("初始化播放器")


if __name__ == "__main__":
    music = MusicPlayer()
    music1 = MusicPlayer()
    print(music is music1)
